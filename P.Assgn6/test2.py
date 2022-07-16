#Factorial of Number Using Recursion

from math import factorial


def fac(a):
       if a<0:return
       elif a == 1:
              return 1
       else:
              return a*fac(a-1)
       
factorial = fac(5)
print (factorial)       