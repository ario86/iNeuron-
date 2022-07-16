#LCM


a=5
b=6

if a>b:
   bigger = a
else:
   bigger = b
   
while(True):
   if(bigger%a==0 and bigger%b==0):
    print(bigger)
    break
bigger += 1        