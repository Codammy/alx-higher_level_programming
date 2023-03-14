#!/usr/bin/python3

def max_integer(my_list=[]):
    _cmp = my_list[0]
    ln = 0
    for i in my_list:
        if i > _cmp:
            _cmp = i
            ln += 1
    if ln == 0:
        return None
    return _cmp
