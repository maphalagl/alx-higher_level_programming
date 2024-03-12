#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        l-digit = number % 10
    else:
        l-digit = number % -10
        l-digit *= -1

    print("{:d}".format(l-digit), end='')
    return (l-digit)
