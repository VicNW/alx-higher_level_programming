#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            print(f"{ord(s) - 32:c}", end='')
        else:
            print(s, end='')
    print()
