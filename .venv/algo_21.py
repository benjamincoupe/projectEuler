"""

Problem 21: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under n.

"""

def sumAmicableNum(n):

    count = 0
    for a in range(1, n):
        divisors_a = [div for div in range(1, a//2 + 1) if a % div == 0]
        sum_a = sum(divisors_a)

        divisors_b = [div for div in range(1, sum_a//2 + 1) if sum_a % div == 0]
        sum_b = sum(divisors_b)

        if sum_b == a and sum_a != a:
            count += sum_a

    return count

print(sumAmicableNum(1000))
print(sumAmicableNum(2000))
print(sumAmicableNum(5000))
print(sumAmicableNum(10000))


# How to upload on Github
