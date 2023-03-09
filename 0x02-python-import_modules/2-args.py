#!/usr/bin/python3

from sys import argv


def cmdarg(argv):
    n = len(argv) - 1
    if n == 1:
        print("{} argument".format(n), end="")
    else:
        print("{} arguments".format(n), end="")
    if n > 0:
        print(":")
    else:
        print(".")

    for i in range(1, n + 1):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    cmdarg(argv)
