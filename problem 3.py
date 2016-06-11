# Problem 3
"""
Description:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
def largest_prime_factor(number):
    largest_factor = 0
    divisor = 2
    while number > 1:
        while number%divisor == 0:
            if divisor > largest_factor:
                largest_factor = divisor
            number /= divisor
        divisor += 1
        if divisor*divisor > number: 
            if number > 1:
                if number > largest_factor:
                    largest_factor = number
                    break
    
    return largest_factor
    

print largest_prime_factor(600851475143)
# End Problem 3