#!/usr/bin/python3

import sys
import calculator_1


def runcal(argv):
    ln = len(argv) - 1
    print(ln, argv[2])
    if ln != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = str(argv[2])

    if operator == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    runcal(sys.argv)
