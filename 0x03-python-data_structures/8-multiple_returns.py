#!/usr/bin/python3

def multiple_returns(sentence):
    # len was not used intentionally
    sig = 0
    for i in sentence:
        sig += 1
    if sig == 0:
        return (sig, None)
    return (sig, sentence[0])
