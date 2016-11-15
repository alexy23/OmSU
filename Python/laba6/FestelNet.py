
def Encrypt (x):
    WorkString = x
    L = []
    R = []
    key = "0101"
    count = 0
    while count < 3:
        L = WorkString[:4]
        R = WorkString[4:]
        WorkString = ""
        ##R = bin((int(R ,2) << 1) ^ (int(R ,2) << 3) ^ int(key,2)).replace('0b','')
        R = bin((int(R ,2) << 1)).replace('0b','')
        if len(R) < 4:
            R = (4 - len(R)) * "0" + R
        WorkString += R
        L = bin(int(L ,2) ^ (int(R ,2))).replace('0b','')
        if len(L) < 4:
            L = (4 - len(L)) * "0" + L
        WorkString += L
        count += 1
    return WorkString

def Decrypt (x):
    WorkString = x
    L = []
    R = []
    key = "0101"
    count = 0
    while count < 3:
        L = WorkString[:4]
        R = WorkString[4:]
        WorkString = ""
        R = bin((int(R ,2) << 1) ^ (int(R ,2) << 3) ^ int(key,2)).replace('0b','')
        WorkString += R
        L = bin(int(L ,2) ^ (int(R ,2))).replace('0b','')
        WorkString += L
        count += 1
    return WorkString