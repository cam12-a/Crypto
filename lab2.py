import re
import io
class lab2:
    openText=""
    data=""
    alphabet=[chr(i) for i in range(ord('А'), ord('Я')+1)]
    matrixAlphabet=[[] for i in range(len(alphabet))]
    for i in range(len(alphabet)):
        matrixAlphabet[i]=[chr(j) for j in range(ord('А'), ord('Я')+1)]
    def __init__ (self,fileName):
        with open(fileName, 'r',encoding='UTF-8') as file:
            self.openText = file.read().replace('\n', '')
        self.openText=self.openText.upper()
        self.openText = re.sub(r'[^\w\s]', '', self.openText)
        self.openText=self.openText.replace(" ","")
        #generation table tritemy
        for i in range(len(self.alphabet)):
            for j in range(len(self.alphabet)):
                self.matrixAlphabet[i][j]=self.alphabet[(i+j)%32]
        #print(self.matrixAlphabet)
    def tritemy(self):
        textCipher=""
        for i in range(len(self.openText)):
            if(self.openText[i]==' '):
                textCipher+=" "
            elif self.openText[i]==',':
                textCipher+=","
            else:
                'print(self.openText[i],i+1, self.alphabet.index(self.openText[i])+1,(i+1+self.alphabet.index(self.openText[i]))%32)'
                textCipher+=self.alphabet[(i+self.alphabet.index(self.openText[i]))%32]
        return textCipher
    def belazo(self,key):
        key=self.normalizeKey(key)
        key=key.upper()
        textCipher=""
        for i in range(len(self.openText)):
                try:
                    #Recherche de la position des lettres dans le text ouvert et la dans la cle
                    indexOfOpenText=self.alphabet.index(self.openText[i])
                    indexofKey=self.alphabet.index(self.matrixAlphabet[0][self.matrixAlphabet[0].index(key[i])])
                    textCipher+=self.matrixAlphabet[indexOfOpenText][indexofKey]
                    #print(indexofKey, indexOfOpenText)
                except (ValueError):
                    continue
        return textCipher
    def vigener(self,key):
        key=self.normalizeKey(key)
        key=key.upper()
        textCipher=""
        for i in range(len(self.openText)):
            #print(self.alphabet.index(key[i]),self.alphabet.index(self.openText[i]))
            textCipher+=self.alphabet[(self.alphabet.index(key[i])+self.alphabet.index(self.openText[i]))%32]
        return textCipher
    def normalizeKey(self,key):
        len_key=0
        new_key=""
        if(len(self.openText)<len(key)):
            len_key=len(self.openText)
        else:
            for i in range(len(self.openText)):
                new_key+=key[i%len(key)]
            key=new_key
        return key
    def descriptVegener(self,textCipher,key):
        textOrigine=""
        key=self.normalizeKey(key)
        key=key.upper()
        textCipher=textCipher.upper()
        for i in range(len(textCipher)):
            textOrigine+=self.alphabet[(self.alphabet.index(textCipher[i])-self.alphabet.index(key[i]))%32]
        return textOrigine
    def decodeTextTritemy(self,textCipher):
        textOrigin=""
        textCipher=textCipher.upper()
        for i in range(len(textCipher)):
            textOrigin+=self.alphabet[(self.alphabet.index(textCipher[i])-i)%32]
        return textOrigin
    def cryptoAnalyseVegenere(self,textCipher):
        return 'fsdgf'
crypt=lab2('crypto/variant.txt')
print("Encryption by Tritemy "+crypt.tritemy())
print("Origine text Tritemy "+crypt.decodeTextTritemy(crypt.tritemy()))
print("Encryption by belazo "+crypt.belazo('ЗОНД'))
print("Encryption by vegenere "+crypt.vigener('ЗОНД'))
print("Origine text vegenere and Belazo "+crypt.descriptVegener(crypt.vigener('ЗОНД'),'ЗОНД'))

