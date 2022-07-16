#Fibonacci Sequence Using Recursion?


def fib(a):
    if (a==0) or (a==1):
        return a
    else:
        return(fib(a-1) + fib(a-2))
        
for i in range(10):
   print(fib(i))