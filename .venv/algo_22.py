"""

Problem 22: Names scores

Using names, an array defined in the background containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the array?

"""

def namesScores(arr):

    arr = sorted(arr)
    scores = []
    multiplier = 1
    letter_values = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
        'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }

    for name in arr:

        alphabetical_value = 0

        for letter in name:
            alphabetical_value += letter_values[letter.upper()]

        scores += [alphabetical_value * multiplier]
        multiplier += 1


    return sum(scores)

print(namesScores(['THIS', 'IS', 'ONLY', 'A', 'TEST']))
print(namesScores(['I', 'REPEAT', 'THIS', 'IS', 'ONLY', 'A', 'TEST']))