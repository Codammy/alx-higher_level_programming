#!/usr/bin/python3
# Data structures to use
units = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9}
tens = {"X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90}
hundreds = {"C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900}
thousands = {"M": 1000, "MM": 2000, "MMM": 3000}

# count decimal_places
def countDp(n):
    i = 0
    while n > 0:
        i += 1
        n = int(n / 10)
    return i

#functions
def isUnit(n):
    for k, v in units.items():
        if v == n:
            return k
def isTens(n):
    for k, v in tens.items():
        if v == n:
            return k
def isHundredth(n):
    for k, v in hundreds.items():
        if v == n:
            return k
def isThousands(n):
    for k, v in thousands.items():
        if v == n:
            return k

#main function
def number_to_romans(number):
    if number <= 9:
        return isUnit(number)
    if number <= 90 and number % 10 == 0:
        return isTens(number)
    if number <= 900 and number % 100 == 0:
        return isHundredth(number)
    if number <= 3000 and number % 1000 == 0:
        return isThousands(number)
    else:
        dcp = 10 ** (countDp(number) - 1)
        number_list = list()
        while (dcp > 0):
            number_list.append(number - (number % dcp))
            number = number % dcp
            dcp = int(dcp / 10)
        str = ""
        pos = len(number_list)
        for li in number_list:
            if pos == 4:
                str += isThousands(li)
            elif pos == 3:
                str += isHundredth(li)
            elif pos == 2:
                str += isTens(li)
            else:
                str += isUnit(li)
            pos -= 1
    return str
