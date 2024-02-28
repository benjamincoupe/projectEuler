"""

Problem 15: Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
6 routes to the bottom right corner.
a diagram of 6 2 by 2 grids showing all the routes to the bottom right corner

How many such routes are there through a given gridSize?

"""

import math

def latticePaths(gridSize):

    m = gridSize
    n = 2 * m
    return int(math.factorial(n) / (math.factorial(m) * math.factorial(n - m)))

print(latticePaths(4))
print(latticePaths(9))
print(latticePaths(20))




