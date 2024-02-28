"""

Problem 16: Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^exponent?

"""

def powerDigitSum(exponent):
    summed = 0
    total = str(2**exponent)
    for digit in total:
        summed += int(digit)

    return summed

print(powerDigitSum(15))
print(powerDigitSum(128))
print(powerDigitSum(1000))
