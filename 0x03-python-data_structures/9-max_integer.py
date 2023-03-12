#!/usr/bin/python3

def max_integer(my_list=[]):
    _cmp = 0
    for i in my_list:
        if i > _cmp:
            _cmp = i
    if _cmp == 0:
        return None
    return _cmp
