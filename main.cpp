#include "readFile.h"
// #include "invertedIndex.h"

#include <iostream>
#include <vector>

using namespace std;

#include "Movie.h"

int main () {
    vector<Movie*>* movies = readFile("./Docs/movies.txt");

    int size = movies -> size();

    for (int i = 0 ; i < size ; ++i) {
        Movie* movie = (*movies)[i];

        cout << movie -> getName() << endl;
        cout << movie -> getDescription() << endl;
    }


    return 0;
}