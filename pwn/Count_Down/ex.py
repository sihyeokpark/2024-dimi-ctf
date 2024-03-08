from pwn import *

p = remote("127.0.0.1", 26146)
#p = process("./Count_down")

p.sendlineafter(" > ", b'\x05\x04\x03\x02\x01')

p.interactive()
