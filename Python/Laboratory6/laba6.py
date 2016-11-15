import FestelNet
# coding: utf8
import codecs
import struct
Select = input('1 - Encrypt\r\n2 - Decrypt')
StringFileInput = raw_input(u'Введите имя файла:')
StringFileInput = 'C:\\' + StringFileInput + '.txt'
WorkString = open(StringFileInput ,'rb').read()
FullString = ""
List = []
Score = ""
BinString = ""
for ch in WorkString:
    TempText = bin(ord(ch))
    TempText = TempText.replace('0b','')
    if len(TempText) < 8:
        TempText = (8 - len(TempText)) * "0" + TempText
    if Select == 1:
        Score = Encrypt(TempText)
        FullString += Score
    elif Select == 2:
        Score = Decrypt(TempText)
        FullString += Score
List = [FullString[i:i + 8] for i in range(0,len(FullString),8)]
List = [chr(int(s , 2)) for s in List]
string = ''.join(List)
StringFileOutput = raw_input(u'Введите имя файла:')
File = open('C:\\' + StringFileOutput + '.txt','wb')
File.write(string)
print(u'Файл %s создан успешно!' %(StringFileOutput))
File.close()