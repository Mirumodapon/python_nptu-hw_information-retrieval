#ifndef _INVERTED_INDEX_
#define _INVERTED_INDEX_

#include <string>
#include <fstream>

#include "Movie.h"
#include "MoviesSet.h"
#include "TermMap.h"
#include "Exception.h"

#include <iostream> // ! temp

class InvertedIndex {
private:
    MoviesSet* movies;
    TermMap* invertedList;

public:
    InvertedIndex() {
        this->movies = new MoviesSet();
        this->invertedList = new TermMap();
    }
    void readFile(std::string path) {
        std::fstream file;
        file.open(path, std::ios::in);

        if (!file) throw Exception("Can\'t open the file.");

        while (!file.eof()) {
            std::string line, name, description;
            getline(file, line);
            if (line == "") continue;

            // split line and assign to name description

            Movie* movie = new Movie("", line);
            std::cout << movie;
            movies->push(movie);
        }
    }
    void inverted();
    MoviesSet* query(std::string term);
};

#endif
