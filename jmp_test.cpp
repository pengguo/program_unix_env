#include <stdio.h>
#include <setjmp.h>

const static int MAX_LEN = 1024;

void do_line(const char *cmd, int &j);
int  cmd_add(int &j);
int get_idx(void);

jmp_buf jmp_buffer;

int main()
{
    char line[MAX_LEN];
    int var_jmp = 1;
    printf("before jmp, var_jmp=%d\n", var_jmp);
    printf("setjmp,return=%d\n", setjmp(jmp_buffer));
    printf("after jmp, var_jmp=%d\n", var_jmp);
    while (fgets(line, MAX_LEN, stdin) != NULL)
        do_line(line, var_jmp); 

    return 0;
}

void do_line(const char *cmd, int &j)
{
    printf("user input:%s\n", cmd);
    j = 2;
    cmd_add(j); 
}

int  cmd_add(int &j)
{
    j = 3;
    if (1 == get_idx())
    {
        printf("in cmd_add, 1 == get_idx()\n");
        longjmp(jmp_buffer, 10);
    }
}
    

int get_idx()
{
    return 1;
}
