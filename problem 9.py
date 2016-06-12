# Problem 9
"""
Description:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
import math

def problem_9():
    for a in range(1,1000):
        for b in range(a+1,1000):
            c1 = 1000 - a - b
            if c1 < b:
                break
            else:
                c2 = math.sqrt(a**2 + b**2)
                if c1 == c2:
                    return a*b*c1

    return -1
    
    
print problem_9()

# End problem 9
