#include "readFile.h"
#include "invertedIndex.h"

#include <iostream>
#include <vector>

using namespace std;

#include "Movie.h"

int main () {
    vector<Movie*>* movies = readFile("./Docs/movies.txt");
    InvertedIndex invertedIndex;

    cout << "Hello 2" << endl; // ! temp
    invertedIndex.insertMovies(*movies);
    cout << "Hello 3" << endl; // ! temp
    invertedIndex.getTermInvertedIndex("movie");
    cout << "Hello 4" << endl; // ! temp



    return 0;
}