#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        sp = 0
        for j in i:
            sp += 1
            print("{:d}".format(j), end="")
            if sp != len(i):
                print(" ", end="")
        print()
