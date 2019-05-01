#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

extern char **environ;

int main()
{
	char *argv[2];
	argv[0] = "/usr/bin/env";
	argv[1] = NULL;
	char *envp[] = {"1","2",NULL};
	execve("/usr/bin/env", argv, envp);

	return 0 ;
}
