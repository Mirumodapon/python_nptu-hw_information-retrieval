#ifndef _MOVIE_
#define _MOVIE_


#include <string>
#include <algorithm>
#include <iostream>

class Movie {
private:
    std::string name;
    std::string description;

public:
    Movie() {}
    Movie(std::string _name) : name(_name) {}
    Movie(std::string _name, std::string _description) :name(_name), description(_description) {}

    friend std::ostream& operator<<(std::ostream& ost, Movie* movie) {
        return ost << movie->name << ": " << movie->description << std::endl;
    }

};


#endif