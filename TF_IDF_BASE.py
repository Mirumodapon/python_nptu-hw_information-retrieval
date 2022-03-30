from math import log10
from Docs import Docs

class TF_IDF_BASE:
    def __init__(self):
        self._docs = list()
        self._size = 0

    def appendDocs(self, doc):
        if (type(doc) != Docs): raise 'Type Error.'
        self._size += 1
        self._docs.append(doc)
    def printDocs(self):
        for doc in self._docs:
            print(doc)

    def _tf(self, word):
        return [doc.count(word) for doc in self._docs]
    def _df(self, word):
        return [1 for doc in self._docs if doc.isInclude(word)]
    def _idf(self, word):
        df = self._df(word)
        return log10(self._size / df) if df != 0 else 0
    def _maxi(self, word):
        tf = self._tf(word)
        return max(tf) if len(tf) != 0 else 0.001
    
    def query(self, q, docsTermWeight, queryTermWeight):
        pass