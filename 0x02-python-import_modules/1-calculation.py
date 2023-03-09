#!/usr/bin/python3

import calculator_1

a = 10
b = 5
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, a + b))
    print("{} - {} = {}".format(a, b, a - b))
    print("{} * {} = {}".format(a, b, a * b))
    print("{} / {} = {:.0f}".format(a, b, a / b))
