#ifndef _READ_FILE_
#define _READ_FILE_

    #include <fstream>
    #include <string>
    #include "Movie.h"

    #include <iostream> // ! temp
    #include <vector>

    std::vector<Movie*>* readFile (std::string path) {

        std::fstream file;
        file.open(path, std::ios::in);

        if (!file) throw "Can not open the file.\n";

        std::vector<Movie*>* movies = new std::vector<Movie*>();
        while (!file.eof()) {
            std::string movie_str;
            getline(file, movie_str);

            Movie* movie = new Movie(movie_str);
            movies -> push_back(movie);
        }

        return movies;
    }


#endif