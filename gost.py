import secrets
import numpy.random
import itertools
from sys import getdefaultencoding
class Gost(object):
  def __init__(self, key, sbox):
    assert self._bit_length(key) <= 256
    self._key = None
    self._subkeys = None
    self.key = key
    self.sbox = sbox

  @staticmethod
  def _bit_length(value):
    return len(bin(value)[2:]) #remove '0b' at start



  @property
  def key(self):
      return self._key

  @key.setter
  def key(self, key):
    assert self._bit_length(key) <= 256
    #Для генерации подключей исходный 256-битный ключ разбивается на восемь 32-битных блоков: K1…K8.
    self._key = key
    self._subkeys = [(key >> (32 * i)) & 0xFFFFFFFF for i in range(8)] #8 кусков


  def _f(self, part, key):
    """Функция шифрования (выполняется в раудах)"""
    assert self._bit_length(part) <= 32
    assert self._bit_length(part) <= 32
    temp = part ^ key #складываем по модулю
    output = 0
    #разбиваем по 4бита
    #в рез-те sbox[i][j] где i-номер шага, j-значение 4битного куска i шага
    #выходы всех восьми S-блоков объединяются в 32-битное слово
    for i in range(8):
      output |= ((self.sbox[i][(temp >> (4 * i)) & 0b1111]) << (4 * i))
      #всё слово циклически сдвигается влево (к старшим разрядам) на 11 битов.
    return ((output >> 11) | (output << (32 - 11))) & 0xFFFFFFFF

  def encrypt(self, plain_msg):
    """Шифрование блока"""

    def _encrypt_round(left_part, right_part, round_key):
      return right_part, left_part ^ self._f(right_part, round_key)

    assert isinstance(plain_msg, int)
    assert self._bit_length(plain_msg) <= 64
    #блок сначала разбивается на две половины
    #(младшие биты — rigth_path, старшие биты — left_path)
    left_part = plain_msg >> 32
    right_part = plain_msg & 0xFFFFFFFF
    #Выполняем 32 рауда со своим подключом Ki
    #Ключи K1…K24 являются циклическим повторением ключей K1…K8 (нумеруются от младших битов к старшим).
    for i in range(24):
      left_part, right_part = _encrypt_round(left_part, right_part, self._subkeys[i % 8])
      #Ключи K25…K32 являются ключами K1…K8, идущими в обратном порядке.
    for i in range(8):
      left_part, right_part = _encrypt_round(left_part, right_part, self._subkeys[7 - i])
    return (left_part << 32) | right_part #сливаем половинки вместе

  def decrypt(self, crypted_msg):
    """Дешифрование блока
    Расшифрование выполняется так же, как и зашифрование, но инвертируется порядок подключей Ki."""

    def _decrypt_round(left_part, right_part, round_key):
      return right_part ^ self._f(left_part, round_key), left_part

    assert isinstance(crypted_msg, int)
    assert self._bit_length(crypted_msg) <= 64
    left_part = crypted_msg >> 32
    right_part = crypted_msg & 0xFFFFFFFF
    for i in range(8):
      left_part, right_part = _decrypt_round(left_part, right_part, self._subkeys[i])
    for i in range(24):
      left_part, right_part = _decrypt_round(left_part, right_part, self._subkeys[(7 - i) % 8])
    return (left_part << 32) | right_part #сливаем половинки вместе

class DerivatedClass(object):
  def __init__(self, alphabet, key, sbox):
    self.gost = Gost(key, sbox)
    self.alphabet = [''] + [chr(i) for i in range(ord('а'),ord('я')+1)] + [' ']
    for i in range(ord('А'),ord('Я')+1):
      self.alphabet.append(chr(i))
    self.alphabet.append(',')
    self.alphabet.append('.')
    self.alphabet.append(':')
    self.alphabet.append('-')
    self.alphabet.append(';')
    
  @staticmethod
  def _devidetextByNCharacters(s, n):
    for start in range(0, len(s), n):
      yield s[start:start+n]
  
  def _convertStrToInt(self, s):    
    return int.from_bytes(list(map(lambda x: self.alphabet.index(x), list(s))), byteorder='big')
  def ConvertIntToStr(self, i):
    return ''.join(self.alphabet[x] for x in i.to_bytes(8, byteorder='big'))
  
  @staticmethod
  def _to_raw(i):
    return ' '.join(bin(x)[2:].zfill(8) for x in i.to_bytes(8, byteorder='big'))
  @staticmethod
  def _from_raw(s):
    return [int(x, 2) for x in s.split(' ')]

  def encrypt_text(self, text):
    chunks = [self._convertStrToInt(x) for x in self._devidetextByNCharacters(text, 8)]
    return ' '.join(self._to_raw(self.gost.encrypt(x)) for x in chunks)

  def decrypt_text(self, text):
    chunks = [int.from_bytes(xx, byteorder='big') for xx in self._devidetextByNCharacters(self._from_raw(text), 8)]
    return ''.join(self.ConvertIntToStr(self.gost.decrypt(x)) for x in chunks)
#@title Сгенерировать ключ
key = secrets.randbits(256)



alphabet = [''] + [chr(i) for i in range(ord('а'),ord('я')+1)] + [' ']
for i in range(ord('А'),ord('Я')+1):
   alphabet.append(chr(i))
# Исходный текст
alphabet.append(',')
alphabet.append('.')
alphabet.append(':')
alphabet.append('-')
alphabet.append(';')
#считение сообщения из файла
def formatText(fileName):
        openText=fileName
        with open(fileName, 'r',encoding="UTF-8") as file:
            openText = file.read().replace('\n', '')
        #openText = sub(r'[^\w\s]', '', openText)
        #opentext=openText.replace(" ","")
        return openText

text=formatText("C:/Users/camar/OneDrive/Desktop/Master/Crypto/Crypto-master/Crypto-master/variant.txt")
# кодировка открытого текста в ascii 
text.encode('ascii', errors='backslashreplace')
filtered_text = ''.join(filter(lambda x: x in alphabet, text.lower()))

#Таблица замен
def SBlock():
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

print("Ключ ",key)

sblock=SBlock()
print("Таблица замены ")
print('sbox = (')
for l in sblock:
  print('  (', ', '.join(str(x) for x in l), '),')
print(')')

gost = DerivatedClass(alphabet, key, sblock)

encrypted_text = gost.encrypt_text(text)
print("Исходный текст:\n", filtered_text)
print("Зашифрованный текст :", encrypted_text)
decrypted_text = gost.decrypt_text(encrypted_text)
print("Расшифрованный текст:", decrypted_text)