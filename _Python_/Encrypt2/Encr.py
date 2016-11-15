##6
##1
##2
##5
##3
##4
def Encrypt(x):
    BuiltString = ""
    Crypt = ""
    for i in x:
        if len(i) < 6:
            BuiltString += i
        else:
            Crypt += i[5]
            Crypt += i[0]
            Crypt += i[1]
            Crypt += i[4]
            Crypt += i[2]
            Crypt += i[3]
            BuiltString += Crypt
            Crypt = ""
    return BuiltString
def Decrypt(x):
    BuiltString = ""
    Crypt = ""
    for i in x:
        if len(i) < 6:
            BuiltString += i
        else:
            Crypt += i[1]
            Crypt += i[2]
            Crypt += i[4]
            Crypt += i[5]
            Crypt += i[3]
            Crypt += i[0]
            BuiltString += Crypt
            Crypt = ""
    return BuiltString