"""

Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square
of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first n natural numbers and the square
of the sum.

"""
# This took me like 3 minutes!

def sumSquareDifference(n):
    list1 = [num**2 for num in range(1, n+1)]
    sum1 = 0
    for num in list1:
        sum1 += num

    list2 = [num for num in range(1, n+1)]
    sum2 = 0
    for num in list2:
        sum2 += num
    sum2 = sum2**2

    return sum2 - sum1

print(sumSquareDifference(10))
print(sumSquareDifference(20))
print(sumSquareDifference(100))
