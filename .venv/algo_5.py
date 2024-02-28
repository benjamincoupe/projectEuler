"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?

"""

def smallestMult(n):

    prime_product = 1
    for num in range(2, n + 1):
        if num > 0 and n % num == 0:
            prime_product *= num

    divisors = [num for num in range(2, n+1)]
    for num in reversed(divisors):
        for _ in divisors:
            if num % _ == 0 and _ != n:
                divisors.remove(_)
    max_num = 10**100
    min_num = prime_product

        # Work with the step size of this loop. Should it be multiples of the largest divisor?
    for product in range(min_num, max_num, divisors[-1]):
        factors = set()
        for num in divisors:

            if product % num == 0:
                factors.add(num)
            if len(factors) == len(divisors):
                return product


print(smallestMult(5))
print(smallestMult(7))
print(smallestMult(10))
print(smallestMult(13))
print(smallestMult(20))
