def murmur3(data, seed = 21):
    c1 = 0xcc9e2d51
    c2 = 0x1b873593

    length = len(data)
    h1 = seed
    roundedEnd = (length & 0xfffffffc)

    for i in range(0, roundedEnd, 4):
        k1 = (ord(data[i]) & 0xff) | ((ord(data[i + 1]) & 0xff) << 8) | \
             ((ord(data[i + 2]) & 0xff) << 16) | (ord(data[i + 3]) << 24)
        k1 *= c1
        k1 = (k1 << 15) | ((k1 & 0xffffffff) >> 17) # замена rotl32(k1,15)
        k1 *= c2

        h1 ^= k1
        h1 = (h1 << 13) | ((h1 & 0xffffffff) >> 19)  # замена rotl32(h1,13)
        h1 = h1 * 5 + 0xe6546b64

    k1 = 0

    val = length & 0x03

    if val == 3:
        k1 = (ord(data[roundedEnd + 2]) & 0xff) << 16

    if val in [2, 3]:
        k1 |= (ord(data[roundedEnd + 1]) & 0xff) << 8

    if val in [1, 2, 3]:
        k1 |= ord(data[roundedEnd]) & 0xff
        k1 *= c1
        k1 = (k1 << 15) | ((k1 & 0xffffffff) >> 17)  # замена rotl32(k1,15)
        k1 *= c2
        h1 ^= k1

    h1 ^= length
    h1 ^= ((h1 & 0xffffffff) >> 16)
    h1 *= 0x85ebca6b
    h1 ^= ((h1 & 0xffffffff) >> 13)
    h1 *= 0xc2b2ae35
    h1 ^= ((h1 & 0xffffffff) >> 16)

    return h1 & 0xffffffff


# if __name__ == '__main__':
#     msg = input('Enter: ')
#     out = murmur3(msg, 21)
#     print('Hash:', hex(out))

