#!/usr/bin/python3

i = 97
while i <= 122:
    if i == 101 or i == 113:
        i += 1
        continue
    print("{:c}".format(i), end="")
    i += 1
