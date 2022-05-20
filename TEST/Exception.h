
#ifndef _EXCEPTION_
#define _EXCEPTION_


    #include <string>
    #include <exception>


    class Exception : public std::exception {
    public:
        Exception() {
            this -> error = "";
        }
        Exception(std::string error) {
            this -> error = error;
        }
        const char* what () const throw () {
            return this -> error == "" ? "Undefined Error" : this -> error.c_str();
        }

    private:
        std::string error;
    };

#endif