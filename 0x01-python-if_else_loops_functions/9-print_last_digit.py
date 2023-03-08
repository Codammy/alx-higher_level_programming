#!/usr/bin/python3

def print_last_digit(number):
    nn = abs(number)
    nn = nn % 10
    print("{}".format(nn), end="")
    return nn
