"""

Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to given limit inclusive were written out in words, how many letters would be used?

Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""

def numberLetterCounts(limit):
    total = ""
    for num in range(1, limit+1):
        name = ""

        # Single digit check
        if len(str(num)) == 1 or len(str(num)) > 2:
            name += digit_dictionary[int(str(num)[0])]

        # Checks if more than 3 digitis in num (thousands)
        if len(str(num)) == 4:
            if str(num)[-3:] == '000':
                name += 'thousand'
            else:
                name += 'thousandand'

        # Checks if more than 2 digits in num (hundreds)
        if len(str(num)) >= 3:
            if len(str(num)) == 3 and str(num)[-2:] == "00":
                name += 'hundred'
            elif len(str(num)) == 3:
                name += "hundredand"

        #        # Single digit check again for hundreds > to optimize
        if len(str(num)) >= 3 and str(num)[-2:] != "00" and str(num)[-2] == "0":
            name += digit_dictionary[int(str(num)[-1])]


        # Check if 10-19
        if len(str(num)) > 1 and int(str(num)[-2]) == 1:
            name += tens_dictionary[int(str(num)[-2:])]

        # Checks if more than one digit in num AND if 20 or above (exclude 11, 12, 13, etc)
        if (len(str(num)) > 1) and (int(str(num)[-2]) > 1):
            name += twenty_above[int(str(num)[-2])]
            if 12 < num < 20:
                name += teen

            if str(num)[-1] != "0":
                name += digit_dictionary[int(str(num)[-1])]
        #print(name)
        total += name
    return len(total)

digit_dictionary = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

# Can remake this for 13-19
tens_dictionary = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

twenty_above = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}




print(numberLetterCounts(5))
print(numberLetterCounts(150))
print(numberLetterCounts(1000))
