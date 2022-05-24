#ifndef _STRING_SPLIT_
#define _STRING_SPLIT_


#include <string>
#include <vector>

#include <iostream> // ! temp

typedef std::vector<std::string> StringArray;

StringArray split(std::string s, std::string delimiter) {
    StringArray result;
    size_t delimiterSize = delimiter.length();

    for (
        size_t pos = s.find(delimiter);
        pos != std::string::npos;
        pos = s.find(delimiter)
        ) {
        std::string token = s.substr(0, pos);
        result.push_back(token);
        s.erase(0, pos + delimiterSize);
    }

    result.push_back(s);
    return result;
}



#endif