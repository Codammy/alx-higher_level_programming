#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    _cmp = my_list[0]
    for i in my_list:
        if i > _cmp:
            _cmp = i
    return _cmp
