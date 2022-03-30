from TF_IDF import TF_IDF

class Schema(TF_IDF):
    def __documentTermWeight(self, tf, idf):
        return [i * idf for i in tf]
    def __queryTermWeight(self, tf, idf, maxi):
        return (0.5 + 0.5 * tf / maxi) * idf
    def query(self, query):
        return super().query(query, self.__documentTermWeight, self.__queryTermWeight)