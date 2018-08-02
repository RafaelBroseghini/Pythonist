#!/usr/bin/env python

"""
Implementation of number conversion to binary and any
other base.
"""

from pythonds.basic.stack import Stack

def divideBy2(number):
    stack = Stack()
    while number > 0:
        remainder = number%2
        stack.push(remainder)
        number = number//2
    
    res = ""
    while not stack.isEmpty():
        res += str(stack.pop())

    return res

def anyBaseConversion(number,base):
    digits = "0123456789ABCDEF"
    stack = Stack()
    while number > 0:
        remainder = number%base
        stack.push(remainder)
        number = number//base
    
    res = ""
    while not stack.isEmpty():
        res += digits[stack.pop()]

    return res

def main():
    number = int(input("Number to convert to binary and hexadecimal: "))
    binaryNumber = divideBy2(number)
    chosenBaseConversion = anyBaseConversion(number,16)
    print("Base 2:",binaryNumber)
    print("Hexadecimal:",chosenBaseConversion)


if __name__ == '__main__':
    main()
