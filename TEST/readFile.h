#ifndef _READ_FILE_
#define _READ_FILE_

    #include <fstream>
    #include <string>
    #include "Movie.h"
    #include "Exception.h"

    #include <iostream> // ! temp
    #include <vector>

    std::vector<Movie*>* readFile (std::string path) {

        std::fstream file;
        file.open(path, std::ios::in);

        if (!file) throw Exception("Can not open the file.\n");

        std::vector<Movie*>* movies = new std::vector<Movie*>();
        while (!file.eof()) {
            std::string movie_str;
            getline(file, movie_str);            
            Movie* movie;
            try {
                movie = new Movie(movie_str);
                movies -> push_back(movie);
            } catch (Exception& e) {
                std::cerr << e.what() << std::endl; // ! temp
                delete movie;
            }

            std::cout << movie -> getName() << std::endl; // ! temp
        }

        std::cout << "Hello" << std::endl; // ! temp

        return movies;
    }


#endif