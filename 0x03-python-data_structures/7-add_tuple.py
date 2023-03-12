#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    ls = []
    ll = []
    ln = 0
    for i in tuple_a:
        ls.append(i)
        ln += 1
    if ln < 2:
        for i in range(ln, 2):
            ls.append(0)
    ln = 0
    for i in tuple_b:
        ll.append(i)
        ln += 1
    if ln < 2:
        for i in range(ln, 2):
            ll.append(0)
    new_tp = ls[0] + ll[0], ls[1] + ll[1]
    return new_tp
