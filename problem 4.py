# -*- coding: utf-8 -*-
# Problem 4
"""
Description:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(number):
    number = list(str(number))
    for i in range(len(number)/2):# 5 digits = 0,1,2,3,4
        if number[i] == number[len(number)-1-i]:
            continue
        else:
            return False
    return True
    
factor1 = 999
factor2 = 999
highest = 0
for i in reversed(range(100,1000)):
    for j in reversed(range(100,1000)):
        product = i * j
        if is_palindrome(product) and product > highest:
            factor1 = i
            factor2 = j
            highest = product
print str(factor1) + '*' + str(factor2) + '=' + str(highest)
# End problem 4