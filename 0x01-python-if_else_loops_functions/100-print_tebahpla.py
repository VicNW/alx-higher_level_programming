#!/usr/bin/python3

for alpha in range(ord('z'), ord('a') - 1, -1):
    if alpha % 2 == 0:
        diff = 0
    else:
        diff = 32
    print(f'{(chr(alpha - diff))}', end='')
