from collections import Counter
import io

def devide_text(text):
    index=len(text)//2
    return dict({item for i, item in enumerate(text.items()) if i < index}),\
           dict({item for i, item in enumerate(text.items()) if i >= index})

def formatOpenText(fileName):
    opentext=""
    with io.open(fileName, 'r',encoding="UTF-8") as file:
        opentext = file.read().replace('\n', '')
    return opentext

def shenanoEncode(text,value='',codes={}):
    if len(text)!=1:
        a,b=devide_text(text)
        shenanoEncode(a,value+'0',codes)
        shenanoEncode(b,value+'1',codes)
    else:
        codes[text.popitem()[0]]=value
    return codes

def shenanoDecode(text,code,index):
    if len(text) != 1:
        a, b = devide_text(text)
        if code[index] == '0':
            return shenanoDecode(a, code, index + 1)
        else:
            return shenanoDecode(b, code, index + 1)
    else:
        return text.popitem()[0]

data=formatOpenText('/home/kali/crypto/variant.txt')
#data="с кудахтаньем"
if len(data)%2!=0:
    data+="#"
count=Counter(data)
sortByDescend=sorted(set(data), key=lambda value: count[value], reverse=True)
sortByDescend_dict={letter: count[letter] for letter in sortByDescend}
print(count)
shEncode=shenanoEncode(sortByDescend_dict)
encoded = [shEncode[letter] for letter in data]
encoded_bits = ''.join(encoded)
encoded_str = [chr(int(encoded_bits[i:i + 8], 2)) for i in range(0, len(encoded_bits), 8)]
print(sortByDescend,sortByDescend_dict)
print(devide_text(sortByDescend_dict))
print(shenanoEncode(sortByDescend_dict))
print(encoded_str)
print(encoded_bits)
index = 0
decoded_str = ''

while index < len(encoded_bits):
    current = shenanoDecode(sortByDescend_dict, encoded_bits, index)  # расшифровать очередной символ
    decoded_str += current             # добавить его в результат
    index += len(shEncode[current])  # перейти на следующий

print('расшифрованная строка: ', decoded_str)



