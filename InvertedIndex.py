from Movie import Movie
from re import sub as replace

class InvertedIndex:
    def __init__ (self):
        self.movies = None
        self.invertedList = dict()

        ignoreString = '{}!()-;:\'"\, `「」שℵℙ∇—©∆¬Ω√Ø√ß®Å™§•∫∏†≈º¶，ǀ\ǃ∞−【】♥～❤─・…（）‘’�|→–……《》･=“”·+。«»“”！″”„†—•’”<>./?@#$%^&*_~'
        self.regux = f'[{",".join(list(ignoreString))},\s]'


    def readFile(self, path):
        file = open(path, encoding='utf8')
        self.movies = file.readlines()
        file.close()

    def inverted(self):
        for movie in self.movies:
            name = movie.split('\t')[0]
            terms = replace(self.regux, ' ', movie.lower()).split(' ')
            terms = list(set(terms))

            for term in terms:
                if term == '' : continue
                if term not in self.invertedList : self.invertedList[term] = set()
                self.invertedList[term].add(name)

    def query(self, terms):
        terms = replace(self.regux, ' ', terms.lower()).split(' ')
        terms = list(set(terms))

        if len(terms) == 0 : return None

        result = None
        if terms[0] in self.invertedList:
            result = self.invertedList[terms[0]]
        else : result = set()

        for n in range(1, len(terms)):
            if terms[n] in self.invertedList:
                result = result & self.invertedList[terms[n]]

        if len(result) == 0 : return None
        else : return {movie for index, movie in enumerate(result) if index < 3}

