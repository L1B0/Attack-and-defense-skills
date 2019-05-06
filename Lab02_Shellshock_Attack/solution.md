# Shellshock Attack Lab

> Author: 1120162015 李博



## Task1: Experimenting with Bash Function 

### /bin/bash_shellshock

如下图，使用`bash 4.2.0`版本。

![shellshock_version](F:\大三下\攻防对抗技术\images\lab2-task1-shellshock_version.png)

结果如下，可以看到父进程定义的函数被成功传递到子进程，存在`shellshock`漏洞。

![shellshock](F:\大三下\攻防对抗技术\images\lab2-task1-shellshock.png)

###  /bin/bash

如下图，使用`bash 4.3.46`版本。

![bash_version](F:\大三下\攻防对抗技术\images\lab2-task1-bash_version.png)

可以看到在父进程中定义的函数并没有传递到子进程，

![bash](F:\大三下\攻防对抗技术\images\lab2-task1-bash.png)

## Task2: Setting up CGI programs

设置如下图

![setup_cgi](F:\大三下\攻防对抗技术\images\lab2-task2-setup-cgi.png)

## Task3: Passing Data to Bash via Environment Variable

结果如下图

![test_cgi](F:\大三下\攻防对抗技术\images\lab2-task3-test-cgi.png)

远程用户之所以能获取到系统当前shell的环境变量信息，是因为通过`curl`命令访问http://localhost/cgi-bin/myprog.cgi，而`myprog.cgi`的功能就是打印当前shell进程的环境变量。

## Task4: Launching the Shell shock Attack

