class Docs:
    def __init__(self, name, content):
        self.__name = name
        self.__content = content
        self.name = lambda : self.__name
        self.content = lambda : self.__content

    def count(self, word):
        return sum([1 for i in self.__content if word == i])
    def isInclude(self, word):
        return word in self.__content