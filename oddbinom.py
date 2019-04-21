import sys
import math
lines = sys.stdin.readlines()
n = int(lines[0])
def odds(n):
    if n < 1:#base case
        return 0
    level = int(math.log2(n))#number of rows in the first sierpinski triangle
    return 3**level + 2*odds(n - 2**level)#recurse on the remaining rows
print(odds(n))
