#include <stdio.h>
#include <iostream>

class BaseClass
{
public:
    BaseClass(): base_i(1) {}
    virtual void f()
    {
        printf("BaseClass::f()\n");
    }

    int base_i;
};

class DerivedClass : public BaseClass
{
public:
    DerivedClass(): derived_i(2) {}
    virtual void g()
    {
        printf("DerivedClass::g()\n");
    } 

    int derived_i;
};

class ThirdClass : public DerivedClass
{
public:
    ThirdClass() : third_i(3) {}
    virtual void h()
    {
        printf("ThirdClass::h()\n");
    }

    int third_i;
};

typedef void (*ClassPtr)(void);

void f(int _i)
{
    printf("void f(int _i)\n");
}
void f(float _i)
{
    printf("void f(float _i)\n");
}

int main()
{
    f(1);
    ThirdClass third_pro;
    int **v_table = (int **)(&third_pro);
    for (int i = 0; (ClassPtr)v_table[0][i] != NULL; i++)
    {
        ClassPtr f_ptr = (ClassPtr)v_table[0][i];
        f_ptr();
    }
    std::cout << *(int *)v_table[1] << std::endl;
    
    printf("class mem:%x\n", &third_pro);
    return 0;
}
