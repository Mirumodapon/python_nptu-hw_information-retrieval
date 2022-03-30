from math import pow, sqrt

class Docs:
    def __init__(self, name, content):
        self._name = name
        self._content = content
        self.name = lambda : self._name
        self.content = lambda : self._content
        pass
    
    def count(self, word):
        return sum([1 for i in self._content if word == i])

    def isInclude(self, word):
        return word in self._content

    def __str__(self):
        return f'{self._name}\n-\n{self._content}\n\n'

    @staticmethod
    def abs(self):
        result = 0
        words = set(self.content())
        for word in words:
            result += pow(self.count(word), 2)
        return sqrt(result)