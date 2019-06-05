#include <stdio.h>
#include <string>
#include <map>
#include <sys/time.h>

typedef unsigned int uint32_t;
typedef unsigned long uint64_t;

inline uint64_t timecost(struct timeval begin, struct timeval end) {
   return (end.tv_sec - begin.tv_sec)*1000 + (end.tv_usec - begin.tv_usec)/1000; 
}

int main() {
    struct timeval begin,end;
    gettimeofday(&begin, NULL);
    
    std::map<uint32_t, std::string> tmpMap;
    for (int i = 0; i < 10000000; i++) {
       tmpMap.insert(std::make_pair(i, "value"));
    }

    gettimeofday(&end, NULL);

    printf("cost time = %lu(ms)\n", timecost(begin, end)); 

}
