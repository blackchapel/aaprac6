import numpy as np

def encrypt(text,key):
    ptMatrix = [text[i:i+2] for i in range(0,len(text),2)]
    print(ptMatrix)
    res = np.dot(ptMatrix,key).tolist()
    print(res)
    ct = ''.join([chr((i[j] %  26) + 97) for i in res for j in range(len(i))])
    print(ct)
    return res

def decrpyt(cipher,key):
    keyInverse = np.linalg.inv(key)
    res = np.dot(cipher,keyInverse)
    pt = ''.join([chr((int(i[j]) %  26) + 97) for i in res for j in range(len(i))])
    print(pt)

text = input("Enter text : ").lower()
text = [ord(i) - 97 for i in text]
key = [[1,2],[2,3]]
res = encrypt(text,key)
decrpyt(res,key)