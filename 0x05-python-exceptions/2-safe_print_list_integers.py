#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        val = my_list[i]
        try:
            print("{:d}".format(val), end="")
            count += 1
        except Exception:
            continue
    print()
    return count
