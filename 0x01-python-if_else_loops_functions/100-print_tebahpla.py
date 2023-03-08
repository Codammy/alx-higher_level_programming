#!/usr/bin/python3

c = 122
for i in range(26):
    print("{:c}".format(c), end="")
    c -= 1
    if c < 97:
        c += 32
    else:
        c -= 32
