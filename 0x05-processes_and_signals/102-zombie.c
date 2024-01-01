#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - Creates 5 processes
 * Return: returns 0 when sucessful
 */
int main(void)
{
	pid_t pid;
	char zombie = 0;

	while (zombie < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			zombie++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
/**
 * inifinte_while - runs an infinite while loop
 * Return: returns 0 when sucessful
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
