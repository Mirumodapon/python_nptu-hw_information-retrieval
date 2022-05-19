#ifndef _READ_FILE_
#define _READ_FILE_

    #include <fstream>
    #include <string>
    #include "Movie.h"

    #include <iostream>
    #include <vector>

    void readFile (std::string path) {

        std::fstream file;
        file.open(path, std::ios::in);

        if (!file) throw "Can not open the file.\n";

        while (!file.eof()) {
            std::string movie_str;
            getline(file, movie_str);

            Movie* movie = new Movie(movie_str);

            std::cout<< movie -> getName() << std::endl;
            std::cout<< movie -> getDescription() << std::endl;
        }

        return;
    }


#endif