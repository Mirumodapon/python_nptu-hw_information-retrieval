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
        return sum([1 for doc in self._docs if doc.isInclude(word)])
    def _idf(self, word):
        df = self._df(word)
        return log10(self._size / df) if df != 0 else 0
    def _maxi(self, word):
        tf = self._tf(word)
        maxi = max(tf) if len(tf) != 0 else 0.001
        return maxi if maxi != 0 else 0.001
    
    def query(self, _q, docsTermWeight, queryTermWeight):
        result = dict()
        q = Docs('', _q)
        for doc in self._docs:
            qw = dict()
            words = set(_q)
            result[doc.name()] = 0
            for word in words:
                tf = doc.count(word)
                df = self._df(word)
                maxi = self._maxi(word)
                tfq = q.count(word)
                result[doc.name()] += docsTermWeight(tf, self._idf(word)) * queryTermWeight(tfq, df, self._size, maxi)
            result[doc.name()] /= Docs.abs(doc)*Docs.abs(q)
        return result