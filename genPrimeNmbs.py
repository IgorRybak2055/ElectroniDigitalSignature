import math
import random

retNmbs = []

def prime():
    flag = False
    lst = []
    a = random.randint(1500000000, 2000000000)
    for i in range(a,2000000000):
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:
                flag = False
                break
            else:
                flag = True
                continue
        if flag:
            flag = False
            lst.append(i)
            if len(lst) > 500:
                return lst
    return lst


primeNmbs = prime()

for i in range(2):
    retNmbs.append(primeNmbs[random.randint(0, len(primeNmbs))])


