import os
import sys
import properties
import shellcode
import overflow

def Go(binary):
    print("Hi!")
    prop = properties.getProperties(binary)
    print(prop)
    shcd = shellcode.GetShellCode(prop)
    print(shcd)
    overflow.OverFlow(binary,shcd)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.exit(Go(sys.argv[1]))
    else:
        print("%s: <binary>" % sys.argv[0])
    