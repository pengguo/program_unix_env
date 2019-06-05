#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/wait.h>
#include <sys/time.h>

void PrintPid(const char *s)
{   
    printf("[%s] ppid=%u,pid=%u\n", s, (unsigned int)getppid(), (unsigned int)getpid());
}

int main()
{
    pid_t pid;
    pid = fork();
    if (0 == pid)
    {
        PrintPid("child");
        printf("next step: sleep\n");
        while (1)
            sleep(1);
    }
    else  
    {
        PrintPid("parent");
        wait(&pid);
    }
    return 0;
}
