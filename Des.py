from io import open
from re import sub
import binascii
from random import randint
class DES:

    def __init__(self,fileName):
        self.openText=fileName
        with open(fileName, 'r',encoding="UTF-8") as file:
            self.openText = file.read().replace('\n', '')
        self.openText = sub(r'[^\w\s]', '', self.openText)
        self.opentext=self.openText.replace(" ","")

    def openTextToBlock64(self):
        return [self.openText[i:i+64] for i in range(0,len(self.openText),64)]

    def Block64ToTwoBlockOf32(self,text64Block):
        #Если длина некротна 64 дополняем сторку с # до 64 символов 
        if len(text64Block)%64!=0:
            for i in range(len(text64Block),64,1):
                text64Block+='#'
        return [self.str2hex(text64Block[0:32]).hex(),self.str2hex(text64Block[32:64]).hex()]

    def AllBlock64To32Blocks(self):
        blockToReturn=[]
        openTextToLits=self.openTextToBlock64()
        for i in range(len(openTextToLits)):
            blockToReturn.append(self.Block64ToTwoBlockOf32(openTextToLits[i]))
        return blockToReturn


    def generateKey(self):
        alphabet=[chr(i) for i in range(ord('а'),ord('я')+1)]
        key=""
        KEY=""
        for i in range(256):
            j=randint(0,i)
            key+=alphabet[j%32]
        key=[self.str2hex(key[i:i+32]).hex() for i in range(0,len(key),32)]
        KEY=[int(self.str2hex(key[i]),16) for i in range(len(key))]
        #print(KEY,len(KEY[0]))
        return key

    def functionValue(self,LeftSide,Key):
        try:
            LeftSide=int(LeftSide,16)
        except TypeError:
            LeftSide=LeftSide
        Key=Key
        print(LeftSide,Key)
        return LeftSide^Key
        
    def devideTo4bits(self,LeftSide):
        LeftSideDevide=[]
        for i in range(32,4):
            LeftSideDevide.append(LeftSide[i:i+1])
        return LeftSideDevide


    def roundText(self,LeftSide,key):
        RightSide=int(LeftSide,16)
        print("LeftSideDDDDD",self.devideTo4bits(LeftSide))
        for j in range(32):
                for i in range(0,7,1):
                    RightSide=LeftSide
                    LeftSide=RightSide^self.functionValue(LeftSide,int(key[i],16))
        return [LeftSide,RightSide]
    
    def SBlock(self):
        S1=[12,4,6,2,10,5,11,9,14,8,13,7,0,3,15,1]
        S2=[6,8,2,3,9,10,5,12,1,14,4,7,11,13,0,15]
        S3=[11,3,5,8,2,15,10,13,14,1,7,4,12,9,6,0]
        S4=[12,8,2,1,13,4,15,6,7,0,10,5,3,14,9,11]
        S5=[7,15,5,10,8,1,6,13,0,9,3,14,11,4,2,12]
        S6=[5,13,15,6,9,2,12,10,11,7,8,1,4,3,14,0]
        S7=[8,14,2,5,6,9,1,12,15,4,11,0,13,10,3,7]
        S8=[1,7,14,13,0,5,8,3,4,15,10,6,9,12,11,2]
        S=[S1,S2,S3,S4,S5,S6,S7,S8]
        return S
        

    def str2hex(self,s):
        return binascii.hexlify(str.encode(s))
 
    def hex2str(self,h):
        return binascii.unhexlify(h)
    

Des=DES("C:/Users/camar/OneDrive/Desktop/Master/Crypto/Crypto-master/Crypto-master/variant.txt")
textToBlock64=Des.openTextToBlock64()
#print(len(textToBlock64))
print(Des.str2hex(textToBlock64[0]).hex())
aa=Des.Block64ToTwoBlockOf32(textToBlock64[0])

aa=Des.AllBlock64To32Blocks()
print("KEY")
print(Des.generateKey(),len(Des.generateKey()))
print("TEXT")
#print(aa)

#print(Des.functionValue(aa[0][0],Des.generateKey()[0][1]))
#print(int(aa[0][0],16)&int(aa[0][1],16))
#print("dsdsf",type(int(aa[0][0],16)))
print(Des.hex2str(aa[0][0]))
#print(Des.hex2str(aa[0][1]).decode("UTF-8"))
#print(len(Des.hex2str(aa[0][1]).decode("UTF-8")))
#print(type(Des.generateKey()[0][1]))
#print(Des.devideTo4bits(aa[0][0]))
#print(Des.roundText(aa[0][0],Des.generateKey()))