#!/usr/bin/python3

def fizzbuzz():
    i = 0
    while i in range(100):
        i += 1
        if i % 3 == 0:
            print("Fizz", end=" ")
            continue
        if i % 5 == 0:
            print("Buzz", end=" ")
            continue
        if i % (5 * 3) == 0:
            print("FizzBuzz", end=" ")
            continue
        print("{}".format(i), end=" ")
