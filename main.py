from os import listdir
from Docs import Docs
from Utils import printDict

from TF_IDF import TF_IDF

from Schema1 import Schema

docs_path = './Document'
query_path = './Query'

ir = Schema()

for docs in listdir(docs_path)[0:3]:
    file = open(f'{docs_path}/{docs}')
    content = file.read().split('\n')[3:]
    content = ' '.join(content)
    content = Docs.parser(content, ignore=['-1'])
    content = Docs(docs, content)
    ir.appendDocs(content)
    # print(content)

# printDict(ir.tf())
# print('\n=\n', end='')
# printDict(ir.idf())



# for query in listdir(query_path)[:1]:
#     file = open(f'{query_path}/{query}')
#     content = file.read()
#     content = Docs.parser(content, ignore=['-1'])
#     # print(content, end='\n\n')
#     print(ir.query(query))


printDict(ir.documentTermWeight())