#include <stdio.h>
#include <stdlib.h>

extern char **environ;
int main()
{
    const char *_name = "name=guopeng";
    setenv("name", "guopeng", 0);
    fprintf(stderr, getenv("name"));

    //environ is a poionter, point to pointer of value;(name, &value)---->value
    while (environ != NULL)
    {
        fprintf(stderr, *environ);
        (environ)++;
    }
}

