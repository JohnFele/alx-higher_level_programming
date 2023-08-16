#!/usr/bin/python3
def uppercase(str):
    str2 = str
    for i in str:
        if i >= 'a' and i <= 'z':
            str2[i] = chr(ord(i) - 32)
        else: 
            str2[i] = str2 [i]
    print('{}'.format(str2))
