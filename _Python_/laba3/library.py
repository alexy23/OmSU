def gcd(a, b, x, y):
    temp = a
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while b > 0:
        q = a / b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    x = x2
    y = y2
    if y < 0:
        y += temp
    if x < 0:
        x += temp
    return y

def Encrypt(x, alpha, b):
    byte = ord(x)
    bytex = chr((alpha * byte + b) % 32)
    return bytex
