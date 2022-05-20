#ifndef _INVERTED_INDEX_
#define _INVERTED_INDEX_


    #include <map>
    #include <vector>
    #include <string>

    #include "Movie.h"
    #include "utils.h"


    #include <iostream> // ! temp

    typedef std::vector<Movie*> MovieList;
    typedef std::map<std::string,MovieList*> Inverted;

    class InvertedIndex {
    public:
        InvertedIndex() {
            inverted = new Inverted();
        }

        void insertMovie (Movie* movie) {
            std::string buff
                = toLowercase(movie -> getName())
                + ' '
                + toLowercase(movie -> getDescription());

            std::string term = "";
            for (char c : buff) {
                if (c == ' ') {
                    this -> termAttach(term, movie);
                    std::cout<< term << std::endl;
                    term = "";
                    continue;
                }
                term += c;
            }
        }

        void insertMovies (std::vector<Movie*> movies) {
            int size = movies.size();
            for (int i = 0 ; i < size ; ++i)
                this -> insertMovie(movies[i]);
        }

        void getTermInvertedIndex (std::string term) {
            std::cout << (*inverted)[term] << std::endl;
        }

    private:
        Inverted* inverted;

        void termAttach (std::string term, Movie* movie) {
            if (inverted -> find(term) == inverted -> end()) {
                // not exists
                inverted -> insert(std::pair<std::string, MovieList*>(term, new MovieList()));
            }
            // insert the movie in to map elements

            (*inverted)[term] -> push_back(movie);
        }
    };


#endif