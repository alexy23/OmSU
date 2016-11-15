def Encrypt(x):
    _Sblock = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
               [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
               [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
               [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
    CryptText = ""
    for s in x:
        if len(s) < 6:
           CryptText += s
        else:
            strk = (str(s[0]) + str(s[2]))
            strk = int(bin(int(strk,2)),2)
            stb = str(s[1]) + str(s[3]) + str(s[4]) + str(s[5])
            stb = int(bin(int(stb,2)),2)
            tail = str(bin(_Sblock[strk][stb])).replace('0b','')
            if len(tail) < 4:
                tail = (4 - len(tail)) * "0" + tail
            #print("(%d,%d) - %s") % (strk + 1 , stb + 1, tail)
            strk = str(bin(strk)).replace('0b','')
            if len(strk) < 2:
                strk = (2 - len(strk)) * "0" + strk
            fullstr = str(strk) + str(tail)
            #fullstr = int(bin(int(fullstr,2)),2)
            CryptText += fullstr
            strk = int(bin(int(strk,2)),2)
            temp = _Sblock[strk][stb]
##            print(strk,stb,temp,s)
    Cryptolist = [CryptText[i:i + 8] for i in xrange(0,len(CryptText),8)]
##    print(Cryptolist)
    Cryptolist = [chr(int(s , 2)) for s in Cryptolist]
    string = ''.join(Cryptolist)
    return string


def Decrypt(x):
    _Sblock = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
               [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
               [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
               [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
    CryptText = ""
    for s in x:
        if len(s) < 6:
            CryptText += s
        else:
            strk = (str(s[0]) + str(s[1]))
            strk = int(bin(int(strk,2)),2)
            tail = str(s[2]) + str(s[3]) + str(s[4]) + str(s[5])
            tail = int(bin(int(tail,2)),2)
            for i in range(len(_Sblock)):
                   for j in range(len(_Sblock[i])):
                       if _Sblock[strk][j] == tail:
                          temp = j
            temp = str(bin(temp)).replace('0b','')
            if len(temp) < 4:
                temp = (4 - len(temp)) * "0" + temp
            strk = str(bin(strk)).replace('0b','')
            if len(strk) < 2:
                strk = (2 - len(strk)) * "0" + strk
            CryptoString = str(strk[0]) + str(temp[0]) + str(strk[1]) + str(temp[1:])
            CryptText += CryptoString
    Cryptolist = [CryptText[i:i + 8] for i in xrange(0,len(CryptText),8)]
##    print(Cryptolist)
    Cryptolist = [chr(int(s , 2)) for s in Cryptolist]
    string = ''.join(Cryptolist)
    return string
