#ifndef _MOVIE_
#define _MOVIE_

    #include <string>

class Movie {
private:
    std::string name;
    std::string description;

public:
    Movie (std::string _name, std::string _description) {
        name = _name;
        description = _description;    
    }
    Movie (std::string movie) {
        int index = movie.find('\t');
        name = movie.substr(0, index);
        description = movie.substr(index + 1, movie.length() - index);
    }

    void setName (std::string _name) { name = _name; }
    void setDescription (std::string _description) { description = _description; }
    std::string getName () const { return name; }
    std::string getDescription () const { return description; }

};

#endif