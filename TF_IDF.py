from math import log10
from Docs import Docs

class TF_IDF:
    def __init__(self):
        self.__docs = list()
        self.__size = 0
        pass

    def appendDocs(self, name, content):
        self.__docs.append(Docs(name, content))
        self.__size = self.__size + 1

    def __tf(self, word):
        return [doc.count(word) for doc in self.__docs] 
    def __idf(self, word):
        return log10(self.__size / sum([1 for doc in self.__docs if doc.isInclude(word)]))
    def __maxi(self, word):
        return max([1 for doc in self.__docs if doc.isInclude(word)])

    def __documentTermWeight(self, tf, idf):
        pass
    def __queryTermWeight(self, tf, idf, maxi):
        pass
    
    def query(self, q, dt, qt):
        words = list()
        for word in q:
           if word not in words : words.append(word)

        dtw = dict()
        qtw = dict()
        for word in words:
            tfq = sum([1 for i in q if i == word])
            tfd = self.__tf(word)
            idf = self.__idf(word)
            maxi = self.__maxi(word)
            dtw[word] = dt(tfd, idf)
            qtw[word] = qt(tfq, idf, maxi)
        innerProduct = [0] * self.__size
        for word in words:            
            for n in range(self.__size):
                innerProduct[n] += dtw[word][n] * qtw[word]
        return innerProduct