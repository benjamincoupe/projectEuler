"""

Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.

The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the nth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

stumped

import math

def findPermutations(arr):
    # If given 8, 7, 9, return 879 and 897
    permutations = []
    if type(arr) == list:
        for num in arr:
            remaining = [x for x in arr if x != num]
            sub_permutations = findPermutations(remaining)
            for perm in sub_permutations:
                permutations.append([num] + perm)

    return permutations

print(findPermutations([7,8,9]))

def lexicographicPermutations(n):

    original = [num for num in range(n)]

    permutation = 1
    pointer_right = 1
    pointer_left = 2

    # Create a recursive function that permutates all the numbers after a number (creates a list from number not including to end of original)
    #

    while permutation < n:
        new = original.copy()

        value_1 = original[-pointer]
        value_2 = original[-pointer - 1]

        if value_1 > value_2:
            # Within this, i must find the permutations keeping the last one there and moving the digits after it
            new[-pointer-1] = value_1
            new[-pointer] = value_2

            pointer += 1
            permutation += 1

            print(original, new, value_1, value_2)

    return original

"""
123456789
123456798
123456879
123456897

123456978
123456987
123457689
123457698
"""

print(lexicographicPermutations(10))