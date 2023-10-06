#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argNum = len(sys.argv) - 1
    if argNum != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opr = str(sys.argv[2])
    if opr not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if opr == '/':
        print("{} {} {} = {}".format(a, opr, b, div(a, b)))
    if opr == '+':
        print("{} {} {} = {}".format(a, opr, b, add(a, b)))
    if opr == '*':
        print("{} {} {} = {}".format(a, opr, b, mul(a, b)))
    if opr == '-':
        print("{} {} {} = {}".format(a, opr, b, sub(a, b)))
