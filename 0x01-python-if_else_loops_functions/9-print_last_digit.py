#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_didgit = -(number)
        last_didgit = last_didgit % 10
        print(last_didgit, end='')
        return(last_didgit)
    else:
        last_digit = number % 10
        print(last_digit, end='')
        return last_digit
