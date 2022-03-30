from os import listdir
from Utils import printDict
from Schema2 import Schema

docs_path = './Document'
query_path = './Query'

ir = Schema()

for docs in listdir(docs_path)[200:500]:
    file = open(f'{docs_path}/{docs}')
    content = file.read().split(' -1\n')[3:]
    content = [word for word in content if word != '']
    ir.appendDocs(docs, content)    


for query in listdir(query_path):
    file = open(f'{query_path}/{query}')
    content = file.read().split(' -1\n')
    content = [word for word in content if word != '']
    print(ir.query(content))



# print(ir.query(['38208 13812 17231 3153 2710 2903 3015 16920']))