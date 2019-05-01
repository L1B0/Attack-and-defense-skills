#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

extern char **environ;

void printenv()
{
	int i = 0;
	while (environ[i] != NULL) {
		printf("%s\n", environ[i]);
		i++;
	}
}

void main()
{
	pid_t childPid;
	switch(childPid = fork()) {
		
		case 0:  /*child process*/
			//printenv();
			//printf("child: %d\n",childPid);
			exit(0);
		default:  /*parent process*/
			printenv();
			//printf("parent: %d\n",childPid);
			exit(0);
	}
}
