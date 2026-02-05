# Latihan Array

Array = [1,9,8,299,390,3,21,34]
kirinya = Array[0]

for i in range(1,len(Array)):
    kanannya=Array[i]
    if kanannya>kirinya:
        kirinya = kanannya

print(kirinya)