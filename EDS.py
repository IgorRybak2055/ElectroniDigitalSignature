import Hash, RSA


def makeAutograph(msg):
    key = RSA.getPrivateKey()
    msg_hash = Hash.murmur3(msg)
    print("Make signature : Private key - ", key, "  Hash - ", msg_hash)

    return pow(msg_hash, key[0], key[1])


def check(msg, autograph):
    key = RSA.getPublicKey()
    msg_hash = Hash.murmur3(msg)
    hash_from_autograph = pow(autograph, key[0], key[1])
    print("Check signature : Public key - ", key, "  Hash - ", hash_from_autograph)


    return "This is a real signature, all is well." if msg_hash == hash_from_autograph else \
           "Problems, the signature is not genuine!"