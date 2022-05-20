#ifndef _INVERTED_INDEX_
#define _INVERTED_INDEX_


    #include <map>
    #include <vector>
    #include <string>

    #include "Movie.h"

    #include <iostream> // ! temp

    typedef std::map<std::string, std::vector<Movie*>> Inverted;

   Inverted* generateInvertedIndex (std::vector<Movie*>& movies) {
        Inverted* inverted = new Inverted();

        
        return inverted;
    }



#endif