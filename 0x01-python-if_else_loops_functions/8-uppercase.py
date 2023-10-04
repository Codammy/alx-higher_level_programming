#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if (c > 96):
            c -= 32
        print("{}".format(chr(c)), end="")
    print()
