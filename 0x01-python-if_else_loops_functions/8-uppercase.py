#!/usr/bin/python3

def uppercase(str):
    for i in str:
        c = ord(i)
        if c > 90:
            c = c - 32
        print("{:c}".format(c), end="")
    print()
