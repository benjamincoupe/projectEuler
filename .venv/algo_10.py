"""

Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below n.

"""

def primeSummation(n):


    integers = [num for num in range(3, n, 2)]
    integers.insert(0, 2)
    for num in integers[1:]:
        if any(num % x == 0 for x in integers[0:integers.index(num)]):
            integers.remove(num)

    return sum(integers)

print(primeSummation(10))

print(primeSummation(17))
print(primeSummation(2001))
print(primeSummation(140759))
#print(primeSummation(2000000))

"""
    primes = set()
    primes.add(2)
    upper_limit = n ** 0.5
    for num in range(3, n, 2):
        if num % 6 == 0:
            continue
        if all(num % prime != 0 for prime in range(3, int(upper_limit) + 1, 2)):
            primes.add(num)"""