#include "readFile.h"
#include "invertedIndex.h"

#include <iostream>
#include <vector>

using namespace std;

#include "Movie.h"

int main () {
    vector<Movie*>* movies = readFile("./Docs/example.txt");
    Inverted* inverted = generateInvertedIndex(*movies);



    return 0;
}