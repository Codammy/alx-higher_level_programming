#!/usr/bin/python3
def safe_print_division(a, b):
    equ = None
    try:
        equ = a / b
    except Exception:
        return equ
    finally:
        print("Inside result: {}".format(equ))
        return equ
