# -*- coding: cp1251 -*-
import codecs
import Crypt

key = input('1 - Encrypt\r\n2 - Decrypt')
fileNameIn = raw_input(u'Введите имя файла для чтения: ')
WorkString = open("C:/" + fileNameIn + ".JPG", 'rb').read()
BinString = ""
for ch in WorkString:
    TempText = bin(ord(ch))
    TempText = TempText.replace('0b','')
    if len(TempText) < 8:
        TempText = (8 - len(TempText)) * "0" + TempText
    BinString += TempText
a = [BinString[i:i+6] for i in xrange(0,len(BinString),6)]
if key == 1:
    _cryptText_ = Crypt.Encrypt(a)
    print "Зашифрован"
elif key == 2:
    _cryptText_ = Crypt.Decrypt(a)
    print "Дешифрован"
fileNameOut = raw_input(u'Введите имя файла для записи: ')
pout = open("C:/" + fileNameOut + ".JPG", 'wb')
for i in _cryptText_:
    pout.write(i)
pout.close()
print('Конец')



