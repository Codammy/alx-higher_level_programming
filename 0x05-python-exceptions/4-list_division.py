#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    res = None
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except Exception:
            res = 0
            if Exception == TypeError:
                print("wrong type")
            elif Exception == ZeroDivisionError:
                print("division by zero")
            elif Exception == IndexError:
                print("out of range")
        finally:
            new_list.append(res)
    return new_list
