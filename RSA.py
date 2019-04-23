import binascii
import random as r
import string
from codecs import encode
import rsa as rsa
from math import gcd, floor

# публичные ключи: d, r
# приватные ключи : p,q, e, d, r

p,q = 11515057, 11518477

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

# print('D = ', d , "R = ", r, "E = ", e)

# alphabet = string.ascii_lowercase
#
# msg = input("Enter message: ")
# nmb_list = list()
#
# for litter in msg:
#     nmb_list.append(int(alphabet.index(litter)+2))
#
#
#
# def encrypt():
#     crypto_list = list()
#     for param in nmb_list:
#         crypto_list.append((param ** e) % r)
#
#     return crypto_list
#
#
# enc = encrypt()
# print("Encrypt message : ", enc)
#
# def my_pow(a, p, m):
#
#     result = 1
#     while p > 2: # когда степень сократится до квадрата и меньше - завершаем
#         if p % 2 == 0: # если степень кратна 2
#             a = (a ** 2) % m
#             p = p // 2 # целочисленное деление (на всякий)
#         else:
#             result = (result * a) % m
#             p = p - 1
#     a = (a ** p) % m
#     result = (result * a) % m
#     return result
#
# def decrypt_f(crypto_list):
#     dec_str = ''
#     # decimal.getcontext().prec = 50
#     for param in crypto_list:
#         tmp = my_pow(param,d,r)
#         dec_str += alphabet[(tmp-2)%26]
#     return dec_str
#
#
# decode_msg = decrypt_f(enc)
# print("Decode = ", decode_msg)


