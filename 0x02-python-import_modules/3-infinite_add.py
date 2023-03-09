#!/usr/bin/python3

from sys import argv


def __sumarg(argv):
    summ = 0
    for i in range(1, len(argv)):
        summ += int(argv[i])
    print(summ)


__sumarg(argv)
