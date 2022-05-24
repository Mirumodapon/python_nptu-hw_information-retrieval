#ifndef _MOVIES_ARRAY_
#define _MOVIES_ARRAY_

#include <set>
#include "Movie.h"

class MoviesSet : public std::set<Movie*> {
private:
public:
    void push(Movie* movie) {
        this->insert(movie);
    }

};


#endif