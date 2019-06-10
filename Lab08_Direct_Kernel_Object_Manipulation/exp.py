#!/usr/bin/python

def u32(s):
        return eval('0x'+s[::-1].encode('hex'))

f = open("./Ubuntu-6c5f5ff8.vmem",'rb')

# 固定大小
pid_size = 4
comm_size = 16
tasks_size = 8

# 固定偏移
pid_offset = 520
comm_offset = 740
tasks_offset = 440

# 0号进程的物理地址
init_task_addr = 0x01863200

#1. read init_task
f.seek(init_task_addr+tasks_offset,0)
next_addr = u32(f.read(4)) - 0xc0000000
print hex(next_addr)

f.seek(init_task_addr+pid_offset,0)
pid = u32(f.read(4))
print hex(pid)

f.seek(init_task_addr+comm_offset,0)
comm = f.read(16)
print comm

# 2. read all proc info
first_comm = comm # 记录第一个进程的comm
while(1):
        f.seek(next_addr+comm_offset-tasks_offset,0)
        comm = f.read(16)
        # 双向链表到达结尾，结束
        if comm == first_comm:
                break
        print "[comm] -> {}".format(comm)
        
        f.seek(next_addr+pid_offset-tasks_offset,0)
        pid = u32(f.read(4))
        print "[pid] -> {}".format(pid)

        f.seek(next_addr,0)
        next_addr = u32(f.read(4)) - 0xc0000000
        print "[next_addr] -> {}".format(hex(next_addr))
