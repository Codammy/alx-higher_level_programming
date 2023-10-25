#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    res = 0
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
                print("wrong type")
        except ZeroDivisionError:
                print("division by zero")
        except IndexError:
                print("out of range")
        finally:
            new_list.append(res)
    return new_list
