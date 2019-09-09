


import os

print(os.path.abspath('gggg.py'))

import time


print(time.time())
print('-------------------')
def chufa(a,b):
    try:
        c = a/b
    except:
        print('除数为0了')
        return
    return c
print(chufa(20,0))

i = open('aaa.txt', 'w')
i.close()

print(i.writelines('fksjfksj'))
