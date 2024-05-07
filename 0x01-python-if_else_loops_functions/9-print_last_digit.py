#!/usr/bin/python3

def print_last_digit(number):
    if (number < 0):
        s = str(number)
        s = s[-1]
        s = int(s)
        print(s, end='')
        return (s)
    else:
        last = number % 10
        print(last, end='')
        return (last)
