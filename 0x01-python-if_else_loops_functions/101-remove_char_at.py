#!/usr/bin/python3

def remove_char_at(str, n):
    newS = ""
    count = 0
    for i in str:
        if n != count:
            newS = newS + i
        count += 1
    return newS
