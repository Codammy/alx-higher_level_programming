#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        len_i = len(i) - 1
        for j in i:
            print("{:d}".format(j), end="")
            if len_i > 0:
                print("", end=" ")
                len_i -= 1
        print()
