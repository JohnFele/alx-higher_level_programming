#!/usr/bin/python3
for i in range(97, 122):
    if i == 'e' or i == 'q':
        continue
    else:
        print('{}'.format(chr(i)), end='')
