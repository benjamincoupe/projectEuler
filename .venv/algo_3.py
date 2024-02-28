"""

Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?

"""

# Retry this one
















def largestPrimeFactor(number):
    # If number is even, it cannot be prime so we find the first odd number from dividing by 2
    while (number % 2 == 0) and (number > 2):
        number //= 2

    # Iterates through odd numbers up to sqrt of number (anything greater than it cannot be a factor)
    for num in range(3, int(number**0.5)+1, 2):
        # If num is a factor, we divide number by it to find the smallest factor
        while number % num == 0 and number > num:
            number //= num

    return number



print(largestPrimeFactor(2))
print(largestPrimeFactor(3))
print(largestPrimeFactor(5))
print(largestPrimeFactor(7))
print(largestPrimeFactor(8))
print(largestPrimeFactor(13195))
print(largestPrimeFactor(600851475143))
