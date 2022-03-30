from TF_IDF import TF_IDF

class Schema(TF_IDF):
    def __init__(self):
        super().__init__()
        self.__documentTermWeight = lambda tf, idf : (1 + tf) * idf
        self.__queryTermWeight = lambda tf, idf, maxi : (1 + tf) * idf

    def documentTermWeight(self):
        return super().documentTermWeight(self.__documentTermWeight)
    pass
