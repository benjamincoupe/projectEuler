"""

Problem 23: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all positive integers <= n which cannot be written as the sum of two abundant numbers.

"""

def sumOfNonAbundantNumbers(n):

    nonabundant = 0
    abundant = set()
    abundant_sums = set()


    for number in range(1, n+1):
        factors = [num for num in range(1, int(number/2) +1) if number % num == 0]
        sum_factors = sum(factors)

        if sum_factors > number:
            abundant.add(number)
            for num in abundant:
                abundant_sums.add(number + num)

    for n in range(1, n+1):
        if n not in abundant_sums:
            nonabundant += n

    return nonabundant

print(sumOfNonAbundantNumbers(10000))
print(sumOfNonAbundantNumbers(15000))
print(sumOfNonAbundantNumbers(20000))
print(sumOfNonAbundantNumbers(28123))

