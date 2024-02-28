"""

Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the nth prime number?

"""

def nthPrime(n):
    next_number = 3
    primes = [2]
    while next_number < 10**100:
        if all(next_number % num != 0 for num in primes):
            primes += [next_number]
        next_number += 1
        if len(primes) == n:
            return primes[-1]

print(nthPrime(6))
print(nthPrime(10))
print(nthPrime(100))
print(nthPrime(1000))
print(nthPrime(10001))




# If num is multiple of 2, not prime. if multiple of 3 not prime, if multiple of 5 not prime etc

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97