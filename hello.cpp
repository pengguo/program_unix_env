#include <stdio.h>
#include <iostream>

void f(void)
{
    printf("void f(void)\n");
}

void f(int _i)
{
    printf("void f(int _i)\n");
}

int main() {
   printf("hello world\n");

   // std::tr1::shared_ptr spr = new std::string("aaa");

   std::cout << "sizeof(long int)" << sizeof(long long) << std::endl; 
   int a = 1;
   int b = 2;
   for (int i = 0; i < 10; i++)
   {
       a++;
   }

   f();
   printf("next step\n");

   a = 101;

   return 0;
}
