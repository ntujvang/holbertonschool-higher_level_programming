#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if number < 0:
    digit = -digit
if digit > 5:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, digit))
elif digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, digit))
elif digit < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, digit))
