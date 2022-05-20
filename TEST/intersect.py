import pandas as pd
import math
import operator
import time
import datetime
import sys
def ReadDoc():
    
    f1=open('.\\movies.txt' , encoding='utf8')
    file=f1.readlines()
    f1.close()
    n=0
    punc = '''!()-[]{};:'"\, `「」שℵℙ∇—©∆¬Ω√Ø√ß®Å™§•∫∏†≈º¶，ǀ\ǃ∞−【】♥～❤─・…（）‘’�|→–……《》･=“”·+。«»“”！″”„†—•’”<>./?@#$%^&*_~'''
    global d_split
    for i in file:
        i=i.replace('\t',' ')
        i=i.strip('\n')
        i=i.lower()
        for b in i:
            #print(b)
            for s in range(len(b)):
                if b[s] in punc:  
                    i=i.replace(b[s],' ')
                if b[s]=='':
                    i=i.replace(b[s],' ')
        a=i.split(' ')
        for b in a:
            if b=='':
                continue
            if b not in d_split:
                d_split[b]=[]
                d_split[b].append(n)               
            else:
                if (d_split[b][-1]!=n):
                    d_split[b].append(n) #d_split[b]=list(set(d_split[b]))使用set執行時間較長          
        n+=1
    d_split=dict(sorted(d_split.items()))
    


def Binary_Search(arr, low, high, x):

	if high >= low:

		mid = (high + low) // 2
		mid=int(mid)
		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return Binary_Search(arr, low, mid - 1, x)
		else:
			return Binary_Search(arr, mid + 1, high, x)

	else:
		return -1

def intersection(a,b):
    i=1
    j=0
    #print('a:',a)
    #print('\nb:',b)
    if len(a)>len(b):
        c=a
        a=b
        b=c
        c=[]
    else:
        c=[]

    for j in range(len(a)):
        #print("\nj:",j)
        if(len(b)==0):
            break
        if a[j]==b[0]  :

            c.append(a[j])
            del b[0]
        elif a[j]<b[0]:
            continue
        else:
            while i<len(b)and b[i]<=a[j] :
                i=i*2
            result=Binary_Search(b,i/2,min(i,len(b)-1),a[j])
            if result != -1:
                c.append(a[j])
                del b[0:result+1]
            else:
                del b[0:i//2+1]
            i=1
        
    return c

def process_query( query):
    query=query.lower()
    query=query.split(' ')
    try:
        a=d_split[query[0]]
    except KeyError :
        a=[]
    for i in range(1,len(query)):
        try:
            b=d_split[query[i]]
            a=intersection(a, b)
            if(len(a)==0):
                break
        except KeyError :
            a=[]
            break
    if(len(a)>2):
        print("交集結果:", a[0:3]) 
    else:
        print("交集結果:", a) 



global d_split
d_split=dict()


start =datetime.datetime.now()     
ReadDoc()
end = datetime.datetime.now()

print("執行時間：" , (end - start))
print("開始時間:",start)
print("結束時間:",end)

query= input('請輸入關鍵字(結束請輸入-1)：')
while(query!='-1'):
    
    process_query(query)
    query= input('請輸入關鍵字(結束請輸入-1)：')

