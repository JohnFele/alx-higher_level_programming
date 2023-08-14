#!/usr/bin/python3
for i in range (0,10):
    for j in range (i+1,10):
        if i != j and i+j != 17:
            print(f'{i:d}{j:d}, ', end='')
        else:
            print(f'{i:d}{j:d}')
