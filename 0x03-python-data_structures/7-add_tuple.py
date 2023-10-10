#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_t1 = len(tuple_a)
    len_t2 = len(tuple_b)
    if len_t1 == 0:
        tuple_a = 0, 0
    elif len_t1 == 1:
        tuple_a = tuple_a[0], 0
    if len_t2 == 0:
        tuple_b = 0, 0
    elif len_t2 == 1:
        tuple_b = tuple_b[0], 0
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
