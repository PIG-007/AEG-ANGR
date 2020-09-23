from pwn import *

def GetShellCode(properties):
    shellcode = b''
    if properties["arch"] == "amd64":
        context(log_level = 'debug', arch = 'amd64', os = 'linux')
        shellcode=asm(shellcraft.sh()) 
    elif properties["arch"] == "i386":
        context(log_level = 'debug', arch = 'i386', os = 'linux')
        shellcode=asm(shellcraft.sh())        
    elif properties["arch"] == "arm":
        context(log_level = 'debug', arch = 'arm', os = 'linux')
        shellcode=asm(shellcraft.sh())  
    return shellcode