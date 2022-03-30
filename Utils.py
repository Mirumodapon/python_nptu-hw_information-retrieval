

def printResult(query, result):
    print(query)
    print('-')
    for doc in result:
        if (result[doc] == 0) : continue
        print(f'{doc}: {result[doc]}')