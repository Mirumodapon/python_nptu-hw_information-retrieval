from os import listdir
from Docs import Docs
from Utils import printDict

from TF_IDF import TF_IDF

docs_path = './Document'
query_path = './Query'

ir = TF_IDF()

for docs in listdir(docs_path)[0:3]:
    file = open(f'{docs_path}/{docs}')
    content = file.read().split('\n')[3:]
    content = ' '.join(content)
    content = Docs.parser(content, ignore=['-1'])
    content = Docs(docs, content)
    ir.appendDocs(content)
    # print(content)

printDict(ir.tf())
print('\n=\n', end='')
printDict(ir.idf())