#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number_x = number % 10
if number_x > 5:
    print(f"Last digit of {number} is {number} and is greater than 5")
elif number_x == 0:
    print(f"Last digit of {number} is {num} and is 0")
else:
    print(f"Last digit of {number} is {-num} and is less than 6 and not 0")
