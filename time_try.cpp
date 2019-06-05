#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <sstream>

typedef long uint64_t;

uint64_t GetPetID(int _qps) {
    time_t raw_time;
    struct tm timeinfo = {0};
    char buf[128];

    time(&raw_time);
    localtime_r(&raw_time, &timeinfo);
    strftime(buf, sizeof(buf), "%Y%m%d%H%M", &timeinfo);
    std::stringstream pp;
    pp << buf << _qps;
    uint64_t pet_id = 0;
    pp >> pet_id;
    return pet_id;
}

int main()
{
    int  aa = 11;
    uint64_t pet_id = GetPetID(11);
    std::cout << pet_id << std::endl;
    return 0;
}
