import Encr
# coding: utf8
import codecs
import struct
key = input('1 - Encrypt\r\n2 - Decrypt')
StringFileInput = raw_input(u'Введите имя файла:')
StringFileInput = 'C:\\' + StringFileInput + '.txt'
WorkString = open(StringFileInput ,'rb').read()
List = []
BinString = ""
for ch in WorkString:
    TempText = bin(ord(ch))
    TempText = TempText.replace('0b','')
    if len(TempText) < 8:
        TempText = (8 - len(TempText)) * "0" + TempText
    BinString += TempText
a = [BinString[i:i+6] for i in range(0,len(BinString),6)]
if key == 1:
    Score = Encrypt(a)
    List = [Score[i:i + 8] for i in range(0,len(Score),8)]
    List = [chr(int(s , 2)) for s in List]
    string = ''.join(List)
    StringFileOutput = raw_input(u'Введите имя файла:')
    File = open('C:\\' + StringFileOutput + '.txt','wb')
    File.write(string)
    print(u'Файл %s создан успешно!' %(StringFileOutput))
    File.close()
elif key == 2:
    Score = Decrypt(a)
    List = [Score[i:i + 8] for i in range(0,len(Score),8)]
    List = [chr(int(s , 2)) for s in List]
    string = ''.join(List)
    StringFileOutput = raw_input(u'Введите имя файла:')
    File = open('C:\\' + StringFileOutput + '.txt','wb')
    File.write(string)
    File.close()
    print(u'Файл %s создан успешно!' %(StringFileOutput))
