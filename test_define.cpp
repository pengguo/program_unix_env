#include <stdio.h>
#include <iostream>
#include <string>

std::string para11("guopeng");

#define TEST_CONNECT(pid) (std::cout << para##pid << std::endl);
#define TEST_VAR(pid) (std::cout << #pid << std::endl);
#define TEST_VAR_S(pid) (std::cout << pid << std::endl);

int main()
{
    TEST_CONNECT(11);
    TEST_VAR(11);
    TEST_VAR_S(11);
    return 0;
}
