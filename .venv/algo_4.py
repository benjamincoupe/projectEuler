"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two n-digit numbers.

"""


def largestPalindromeProduct(n):
    if n == 1:
        return
    number1 = int('9'*n)
    number2 = number1
    palindrome = []
    # Keep both numbers from going down by 1 magnitude (if start with 2>99. dont let them try below 89)
    for i in reversed(range(number1 - n*10, number1+1)):
        for num in reversed(range(2, number2+1)):
            product = i * num
            length_product = len(str(product))
            first_half = str(product)[:length_product // 2]
            second_half = str(product)[length_product // 2:]
            second_half = second_half[::-1]
            print(i, num, product, first_half, second_half)
            if first_half == second_half:
                palindrome += [product]
    return max(palindrome)


print(largestPalindromeProduct(3))