num = int(input("Upto"))

n1, n2 = 0, 1
count = 0

if num <= 0:
   print("N/A")
   
elif num == 1:
    print(n1)

else:
   print("fibonacci series:")
   while count < num:
       print(n1)
       a= n1 + n2
       n1 = n2
       n2 = a
       count += 1
