from pwn import*
context(log_level = 'debug', arch = 'x64', os = 'linux')
shellcode=asm(shellcraft.sh())
print(shellcode)
