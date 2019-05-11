import rsa as rsa
from math import gcd
import genPrimeNmbs

# публичные ключи: d, r
# приватные ключи : p,q, e, d, r

p,q = genPrimeNmbs.retNmbs[0], genPrimeNmbs.retNmbs[1]
# print("p == " , p , "\nq == ", q)
def genKeys():
    r = p * q
    phi_r = (p - 1) * (q - 1)

    for i in range(2, pow(2, 512)):
        if gcd(i, phi_r) == 1:
            e = i
            break

    # посчитать d
    d = rsa.common.inverse(e, phi_r)

    return d,e,r


def getKey(delimitation):
    keys = genKeys()
    return [keys[1], keys[2]] if delimitation == 'private' else [keys[0], keys[2]]


def getPrivateKey():
    return getKey("private")


def getPublicKey():
    return getKey("public")



