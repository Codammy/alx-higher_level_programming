#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    t_num = number * (-1)
    ldigit = (t_num % 10) * (-1)
else:
    ldigit = number % 10

print(f"Last digit of {number} is {ldigit}", end=" ")

if ldigit > 5:
    print("and is greater than 5")
elif ldigit < 6 and ldigit != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
