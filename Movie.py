
class Movie:
    def __init__ (self):
        self.name = None
        self.description = None
        pass
    def __init__ (self, name, description):
        self.name = name
        self.description = description
    def __init__ (self, info):
        temp = info.split('\t')
        print(temp)
        if (len(temp) < 2) : assert False, 'Information Format Error.\n'
        self.name = temp[0]
        self.description = temp[1]

    def getFullInfo (self):
        return f'{self.name} {self.description}'
    def __str__ (self):
        return self.getFullInfo()