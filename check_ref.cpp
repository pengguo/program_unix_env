#include <iostream>
#include <string>

std::string global_str("guopeng");

const std::string &GetQrw() {
    std::string &ref1 = global_str;
    return ref1; 
}

int main() {
    global_str = "guopeng_modify";
    const std::string &local_str = GetQrw();
    const std::string &loc2 = GetQrw();
    std::cout << local_str << std::endl;
    std::cout << loc2 << std::endl;


    std::string aa = "guopeng";
    std::cout << aa[2] << std::endl;
}

