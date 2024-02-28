"""

Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

"""

def multiplesOf3Or5(number):
    value = 0
    for num in range(number):
        if (num % 3 == 0) or (num % 5 == 0):
            value += num
    return value

print(multiplesOf3Or5(10))
print(multiplesOf3Or5(49))
print(multiplesOf3Or5(1000))
print(multiplesOf3Or5(8456))
print(multiplesOf3Or5(19564))
