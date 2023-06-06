#!/usr/bin/python3
import random

def check_number(number):
    if number < 0:
        print(f"{number:d} is negative")
    elif number == 0:
        print(f"{number:d} is zero")
    elif number > 0:
        print(f"{number:d} is positive")

number = random.randint(-10, 10)
check_number(number)

