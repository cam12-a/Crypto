data = open('/content/ch7.bin', 'rb').read()
str1=""
for i in data:
  if i!='b':
    str1+=chr(i)
out =""
for index in range(25):
  for d in str1:
    try:
	    out += chr(ord(d)-index)
    except:
      continue
  print(out)
  out=""
  Bravo! Tu peux valider avec le pass Yolaihu
