
from random import randint
import math
import sys
Limit=10000000
#Генерации Алфабета для нахождения хзша
def alpha():
    alphabet = [''] + [chr(i) for i in range(ord('а'),ord('я')+1)] + [' ']
    for i in range(ord('А'),ord('Я')+1):
      alphabet.append(chr(i))
    alphabet.append(',')
    alphabet.append('.')
    alphabet.append(':')
    alphabet.append('-')
    alphabet.append(';')
    return alphabet
#Генерации простых чисел
def generatePrimNumber(Intbetween):
    while True:
        isprime = True
        
        for x in range(2, int(math.sqrt(Intbetween) + 1)):
            if Intbetween % x == 0: 
                isprime = False
                break
        
        if isprime:
            break
        Intbetween += 1
    return Intbetween
#два числа являются ли простыми
def checkIsPGCP(a, b):
    while b:
        a, b = b, a % b
    if a==1:
        return True
    else: return False
#Генерации P & Q
def genertePQ():
    
    p=generatePrimNumber(randint(0,Limit))
    q=generatePrimNumber(randint(0,Limit))

    return p,q
#Генерации ключей 
def generateKeys():
    PQ=genertePQ()
    N=PQ[0]*PQ[1]
    M=(PQ[0]-1)*(PQ[1]-1)

    E=generatePrimNumber(randint(0,Limit))
    D=modinv(E,M)
    return [N,M,D,E,PQ[0],PQ[1]]
#нахождения НОД
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)
#Нахождения обратной модули
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m
#Шифрование сообщения
def encryptRSA(text,E,N):
    textCipher=""
    for i in range(len(text)):
        textCipher+=str(pow(ord(text[i]),E,N))+ " "
   
    return textCipher
#Вычисление хэш
def generateHash(text,N):
    h=0
    for i in range(len(text)):
        h=((h+alpha().index(text[i]))**2)%N
    return h
#Расшифровка сообщения 
def descriptRSA(text,D,N):
    textOpen=""
    parts=text.split()

    for part in parts:
        if part:
            c = int(part)
            textOpen+= chr(pow(c, D, N))
    return textOpen
#чтение файла
def formatText(fileName):
        openText=fileName
        with open(fileName, 'r',encoding="UTF-8") as file:
            openText = file.read().replace('\n', '')
        #openText = sub(r'[^\w\s]', '', openText)
        #opentext=openText.replace(" ","")
        return openText

#print(genertePQ())
text=formatText("C:/Users/camar/OneDrive/Desktop/Master/Crypto/Crypto-master/Crypto-master/text.txt")

print("Исходный текст\n",text)
keys=generateKeys()
print("Открытый ключ {} закрытый ключ {} p= {} q={} N={}".format(keys[3],keys[2],
keys[4],keys[5],keys[0]))
encrypt=encryptRSA(text,keys[3],keys[0])
print("Шифро-сообщения\n",encrypt)
print("Сгенерированный хэш\n",generateHash(text,keys[0]))
descrypt=descriptRSA(encrypt,keys[2],keys[0])
print("Расшифрока сообщения\n",descrypt)