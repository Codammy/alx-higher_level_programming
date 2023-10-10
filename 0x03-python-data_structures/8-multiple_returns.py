#!/usr/bin/python3
def multiple_returns(sentence):
    a = None
    ls = len(sentence)
    if ls >= 1:
        a = sentence[0]
    return ls, a
