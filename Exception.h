#ifndef _EXCEPTION_
#define _EXCEPTION_

#include <exception>
#include <string>

class Exception : public std::exception {
private:
    std::string msg;
public:
    Exception() {
        this->msg = "";
    }
    Exception(const std::string error) : msg(error) {}

    const char* what() const throw () {
        return this->msg == "" ? "Undefined Error." : this->msg.c_str();
    }

};

#endif