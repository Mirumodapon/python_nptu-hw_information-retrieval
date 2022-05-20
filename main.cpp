#include "readFile.h"
#include "invertedIndex.h"

#include <iostream>
#include <vector>

using namespace std;

#include "Movie.h"

int main () {
    vector<Movie*>* movies = readFile("./Docs/example.txt");
    InvertedIndex invertedIndex;

    invertedIndex.insertMovies(*movies);
    invertedIndex.getTermInvertedIndex("doc");
    invertedIndex.getTermInvertedIndex("a");
    invertedIndex.getTermInvertedIndex("movie");
    invertedIndex.getTermInvertedIndex("gd");




    return 0;
}