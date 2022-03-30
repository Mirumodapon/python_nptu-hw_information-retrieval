from re import split

class Docs:
    def __init__(self, name, content):
        self.__name = name
        self.__content = content
        self.getName = lambda : self.__name
        self.getContent = lambda : self.__content
    def __str__(self):
        content = ' '.join(self.__content)
        return f'{self.__name}\n=\n{content}\n\n'

    @staticmethod
    def parser(*documents, ignore=[]):
        temp = []
        for document in documents:
            for word in split('\n', document):
                word = word.replace('-1', '')
                if (not word in ignore):
                    temp.append(word)
        return temp
