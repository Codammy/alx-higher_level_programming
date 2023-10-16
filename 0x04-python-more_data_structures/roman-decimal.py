#!/usr/bin/python3
""" This scripts converts decimal numbers to roman numerals
    it defines it data structure and some functions like units,     tens, hundreds, thousands, isUnit, isTens, isHundredth,
    isThousands and countDp. All these are used for conversion
"""

""" Data structures to use """
units = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9}
tens = {"X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90}
hundreds = {"C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900}
thousands = {"M": 1000, "MM": 2000, "MMM": 3000}


def countDp(n):
    """count decimal_places"""
    i = 0
    while n > 0:
        i += 1
        n = int(n / 10)
    return i


def isUnit(n):
    """returns roman numerals in units"""
    for k, v in units.items():
        if v == n:
            return k
    return ""


def isTens(n):
    """returns romanan numerals in tens"""
    for k, v in tens.items():
        if v == n:
            return k
    return ""


def isHundredth(n):
    """returns romanan numerals in hundreds"""
    for k, v in hundreds.items():
        if v == n:
            return k
    return ""


def isThousands(n):
    """returns romanan numerals in thousands"""
    for k, v in thousands.items():
        if v == n:
            return k
    return ""


def number_to_romans(number):
    """Main function"""
    if type(number) is not int:
        print("Input must be an int")
        quit(1)
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
            n = number - (number % dcp)
            if n != 0:
                number_list.append(n)
            number = number % dcp
            dcp = int(dcp / 10)
        str = ""
        for li in number_list:
            str += isThousands(li)
            str += isHundredth(li)
            str += isTens(li)
            str += isUnit(li)
    return str


# Interactive mode
if __name__ == '__main__':
    decimal = input("Input decimal number, (MIN: 0, MAX: 3999): ")
    try:
        decimal = int(decimal)
    finally:
        print(f"{decimal} - {number_to_romans(decimal)}")
