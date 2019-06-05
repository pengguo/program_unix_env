#include <stdio.h>

const static int MAX_NUM = 17;

int GetLastPeo()
{
    int idx = 0;
    int person_list[MAX_NUM] = {0};
    int cnt = MAX_NUM;

    while (cnt > 1)
    {
        for (int i = 0; (i < MAX_NUM); i++)
        {
           if (person_list[i] == 1) continue;

           idx += 1;
           if (idx % 3 == 0)
           {
               cnt--;
               person_list[i] = 1;
           } 
        }
    }
    for (int i = 0; i < MAX_NUM; i++)
    {
        if (person_list[i] == 0)
        {
            fprintf(stderr, "%d\n", i);
            return i;
        }
    }
    return 0;
}
    

int main()
{
    GetLastPeo();
}
