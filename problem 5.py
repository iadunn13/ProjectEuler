# -*- coding: utf-8 -*-
# Problem 5
"""
Description:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def gcd(a, b):
    # Compute the greatest common divisor of a and b using Euclid's Algorithm
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Compute the least common multiple of a and b
    return a * b // gcd(a, b)

nums = [i+1 for i in range(20)] # list of numbers 1 through 20
print reduce(lcm, nums)

# End problem 5