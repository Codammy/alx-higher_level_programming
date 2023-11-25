#!/usr/bin/python3
""" function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    ln = len(matrix[0])
    nwlist = []
    for row in matrix:
        child = []
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if ln != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for r in row:
            if type(r) is not int and type(r) is not float:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            child.append(float(f"{r / div:.2f}"))
        nwlist.append(child)
        ln = len(row)
    return nwlist
