#cube sum of first n natural numbers

import math

n = int(input("enter a number: "))
n += math.pow(n,3)
print(n)