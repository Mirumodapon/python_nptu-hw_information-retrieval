
from os import listdir
from TF_IDF import TF_IDF, Schema1, Schema2, Schema3
from Docs import Docs
# from re import split


path = {
    'docs': './Document',
    'query': './Query'
}

ir = TF_IDF(Schema1)

for doc in listdir(path['docs'])[:2]:
    file = open(f"{path['docs']}/{doc}", 'r')
    content = file.read().split('\n')[3:]
    content = [word.replace(' -1', '') for word in content if word != '']
    content = Docs(doc, content)
    print(Docs.abs(content))
    ir.appendDocs(content)


for query in listdir(path['query'])[:1]:
    pass

print(ir.query(0))
# ir.printDocs()