"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.

"""

def specialPythagoreanTriplet(n):

    for b in range(2, n-1):
        a = 1

        while a < b-1:
            c = (a ** 2 + b ** 2) ** 0.5

            if a + b + c == n:
                return a*b*c

            a += 1


print(specialPythagoreanTriplet(24))
print(specialPythagoreanTriplet(120))
print(specialPythagoreanTriplet(1000))
