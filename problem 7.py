# Problem 7
"""
Description:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

# simple brute force method
# not super efficient, but 10,001st prime is still fast to compute
# it could modified to skip even numbers, but they fail on the first check so
# they aren't computationally taxing

num = 2 # first prime
prime_set = [num]
while len(prime_set) < 10001:
    is_prime = True
    num += 1
    for prime in prime_set:
        if num%prime == 0:
            is_prime = False
            break # num is not prime
    if is_prime:
        prime_set.append(num) # will only get here if num is prime
print prime_set[10000]
