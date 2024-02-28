"""

Problem 20: Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits n!

"""
# This only took a few minutes


def sumFactorialDigits(n):
    product = 1
    for num in range(1, n+1):
        product *= num

    return sum([int(digit) for digit in str(product)])


print(sumFactorialDigits(10))
print(sumFactorialDigits(25))
print(sumFactorialDigits(50))
print(sumFactorialDigits(75))
print(sumFactorialDigits(100))

