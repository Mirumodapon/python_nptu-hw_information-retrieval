#ifndef _INVERTED_INDEX_
#define _INVERTED_INDEX_


    #include <map>
    #include <vector>
    #include <string>
    #include <algorithm>

    #include "Movie.h"
    #include "utils.h"


    #include <iostream> // ! temp

    typedef std::vector<Movie*> MovieList;
    typedef std::map<std::string,MovieList*> Inverted;

    class InvertedIndex {
    public:
        InvertedIndex() {
            inverted = new Inverted();
            ignore = "\".()[]{}\\/!@#$%^,&*()_+';:?<>=-~!()-[]{};:,`「」שℵℙ∇—©∆¬Ω√Ø√ß®Å™§•∫∏†≈º¶，ǀǃ∞−【】♥～❤─・…（）‘’�|→–……《》･=“”·+。«»“”！″”„†—•’”<>./?@#$%^&*_~`,";
        }

        void insertMovie (Movie* movie) {
            std::string buff
                = toLowercase(movie -> getName())
                + ' '
                + toLowercase(movie -> getDescription());

            std::string term = "";
            for (char c : buff) {
                if (c == ' ' || ignore.find(c) != std::string::npos) {
                    this -> termAttach(term, movie);
                    term = "";
                    continue;
                }
                term += c;
            }

            if (term != "") this -> termAttach(term, movie);
        }

        void insertMovies (std::vector<Movie*> movies) {
            int size = movies.size();
            for (int i = 0 ; i < size ; ++i)
                this -> insertMovie(movies[i]);
        }

        void getTermInvertedIndex (std::string term) {

            std::cout << "======" << std::endl;
            std::cout << "Term: " << term << std::endl;

            MovieList* movies = (*inverted)[term];

            int size = movies -> size();
            for (int i = 0 ; i < size ; ++i) {
                Movie* movie = (*movies)[i];
                std::cout << movie -> getName() << std::endl;
                // std::cout << movie -> getDescription() << std::endl;
            }

            std::cout<< "=====" << std::endl;
        }

    private:
        Inverted* inverted;
        std::string ignore;

        void termAttach (std::string term, Movie* movie) {
            if (term == "") return;
            if (inverted -> find(term) == inverted -> end()) {
                // not exists
                inverted -> insert(std::pair<std::string, MovieList*>(term, new MovieList()));
            }
            // insert the movie in to map elements
            MovieList* movies = (*inverted)[term];
            if (std::find(movies -> begin(), movies -> end(), movie) == movies -> end())
                movies -> push_back(movie);

            std::cout << term << std::endl;
        }
    };


#endif