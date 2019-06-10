# Direct Kernel Object Manipulation

> 1120162015 李博

## Task1: 在虚拟机内部加载内核模块输出进程信息

hello.c代码如下

首先获取`init_task`地址，它是kernel中的第一个进程，以此遍历进程控制块链表，获取进程信息。

```c
#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/sched.h>
#include <linux/init_task.h>
// 初始化函数
static int hello_init(void)
{
    struct task_struct *p;
    p = NULL;
    p = &init_task;
    for_each_process(p)
    {
        if(p->mm != NULL){ // 输出非内核线程
            printk(KERN_ALERT"%s\t%d\n",p->comm,p->pid);
        }
    }
    return 0;
}
// 清理函数
static void hello_exit(void)
{
    printk(KERN_ALERT"goodbye!\n");
}

// 函数注册
module_init(hello_init);  
module_exit(hello_exit);
```

Makefile内容如下

```makefile
ifneq	($(KERNELRELEASE),)
obj-m	:= hello.o 

else
KDIR	:= /lib/modules/$(shell uname -r)/build
PWD	:= $(shell pwd)
default:	
	$(MAKE) -C $(KDIR) SUBDIRS=$(PWD) modules 
	rm -r -f .tmp_versions *.mod.c .*.cmd *.o *.symvers 

endif
```

执行以下命令

![task1-setup](../images/lab8-task1-setup.png)

结果部分如下图

![task1-result](../images/lab8-task1-result.png)



## Task2: 分析虚拟机的内存，输出进程信息

