from io import open
from re import sub
import binascii
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
        return [self.str2hex(text64Block[0:32]),self.str2hex(text64Block[32:64])]

    def AllBlock64To32Blocks(self):
        blockToReturn=[]
        openTextToLits=self.openTextToBlock64()
        for i in range(len(openTextToLits)):
            blockToReturn.append(self.Block64ToTwoBlockOf32(openTextToLits[i]))
        return blockToReturn


    def generateKey(self):
        return [[]]

    def functionValue(self,LeftSide,Key):
        return LeftSide
        


    def str2hex(self,s):
        return binascii.hexlify(bytes(str.encode(s)))
 
    def hex2str(self,h):
        return binascii.unhexlify(h)
    

Des=DES("/home/kali/crypto/text.txt")
textToBlock64=Des.openTextToBlock64()
print(len(textToBlock64))
print(len(Des.str2hex(textToBlock64[0]).decode("UTF-8")))
aa=Des.Block64ToTwoBlockOf32(textToBlock64[0])
'''print(aa)

print(Des.str2hex(aa[0]))
print(Des.str2hex(aa[1]))'''
aa=Des.AllBlock64To32Blocks()
print("dsf",len(aa))
print(Des.hex2str(aa[0][0]).decode("UTF-8"))
print(Des.hex2str(aa[0][1]).decode("UTF-8"))

print(len(Des.hex2str(aa[0][0]).decode("UTF-8")))
print(len(Des.hex2str(aa[0][1]).decode("UTF-8")))