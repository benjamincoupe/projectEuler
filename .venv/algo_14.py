"""

Problem 14: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under the given limit, produces the longest chain?

Note: Once the chain starts the terms are allowed to go above limit.

"""

def longestCollatzSequence(limit):

    max_sequence = [1, [1]]

    for num in range(2, limit+1):

        sequence = [num]

        while sequence[-1] != 1:

            x = sequence[-1]

            if x % 2 == 0:

                sequence += [x // 2]

            elif x % 2 != 0:

                sequence += [3*x + 1]

        if len(sequence) > len(max_sequence[1]):

            max_sequence = [num, sequence]

    return max_sequence[0]


print(longestCollatzSequence(14))
print(longestCollatzSequence(5847))
print(longestCollatzSequence(46500))
print(longestCollatzSequence(54412))
print(longestCollatzSequence(100000))
print(longestCollatzSequence(1000000))
