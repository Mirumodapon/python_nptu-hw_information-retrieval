from TF_IDF_BASE import TF_IDF_BASE

class TF_IDF(TF_IDF_BASE):
    def __init__(self, Schema):
        super().__init__()
        self._docsTermWeight = Schema['docsTermWeight']
        self._queryTermWeight = Schema['queryTermWeight']
    def query(self, q):
        return super().query(q, self._docsTermWeight, self._queryTermWeight)


Schema1 = {
    'docsTermWeight': lambda tf, idf : tf * idf,
    'queryTermWeight': lambda tf, df, size, maxi : (0.5 + 0.5 * tf / maxi) * (log10(size / df) if df != 0 else 0)
}
Schema2 = {
    'docsTermWeight': lambda tf, idf : 1 + tf,
    'queryTermWeight': lambda tf, df, size, maxi : log10(1 + (size / df if df != 0 else 0))
}
Schema3 = {
    'docsTermWeight': lambda tf, idf : (1 + tf) * idf,
    'queryTermWeight': lambda tf, df, size, maxi : (1 + tf) * (log10(size / df) if df != 0 else 0)
}