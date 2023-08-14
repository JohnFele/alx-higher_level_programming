#!/usr/bin/python3
for i in range (97,122):
    i = chr(i)
    if i == 'e' or i == 'q':
        continue
    else:
        print(i, end='')
