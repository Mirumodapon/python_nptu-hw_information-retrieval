#ifndef _UTILS_
#define _UTILS_


    #include <string>
    #include <algorithm>

    std::string toLowercase (std::string str) {
        std::string temp = str;
        std::transform(
            temp.begin(),
            temp.end(),
            temp.begin(),
            [](unsigned char c) {
                return std::tolower(c);
            }
        );
        return temp;
    }


#endif