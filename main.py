from InvertedIndex import InvertedIndex
from datetime import datetime

inverted = InvertedIndex()


timestamp = datetime.now()     
inverted.readFile('./Docs/movies.txt')
inverted.inverted()
timecost = datetime.now() - timestamp

print(f'Execute Time: {timecost}')

while (True):
    query = input('Search: ')
    if query == '_exit_' : break
    print(inverted.query(query))
    print('=====')
