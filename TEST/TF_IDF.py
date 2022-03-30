from Docs import  Docs
from math import log10

class TF_IDF:
    def __init__(self):
        self.__docs = list()
        self.__docsName = list()
        self.__size = 0
        self.__tf = dict()
    def appendDocs(self, docs):
        if (type(docs) != Docs): raise 'Type Error.'
        self.__docs.append(docs.getContent())
        self.__docsName.append(docs.getName())
        self.__size += 1
        for tf in self.__tf:
            self.__tf[tf].append(0)
        for word in docs.getContent():
            if (word not in self.__tf): self.__tf[word] = [0]*self.__size
            self.__tf[word][-1] = sum([1 for term in self.__docs[-1] if term == word])

    def documentTermWeight(self, termWeight):
        idf = self.idf()
        tf = self.tf()
        for word in tf:
            for i in range(len(tf[word])):
                tf[word][i] = termWeight(tf[word][i], idf[word])
        return tf

    def query(self, query):
        if (type(query) == list): return self.__queryMultipleWords(query)
        if (type(query) == str): return self.__querySignalWord(query)
        raise 'Type Error.'

    
    def size(self):
        return self.__size
    def tf(self):
        return self.__tf
    def idf(self):
        idf = dict()
        for word in self.__tf:
            idf[word] = log10(self.__size/sum([1 for doc in self.__docs if word in doc]))
        return idf

    def __queryMultipleWords(self, query):
        pass
    def __querySignalWord(self, query):
        pass