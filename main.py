import EDS

if __name__ == '__main__':
    msg = input("Input your message: ")
    autograph = EDS.makeAutograph(msg)
    print("The signature that turned out : ", autograph)

    print(EDS.check(msg, autograph))
