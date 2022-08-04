#5

a= input("enter str: ")

count = 0

for i in a:
    if i.isalpha():
        count= count+1
    else:
        pass
    

print("LETTERS" ,count)
    
for j in a:
    if j.isdigit():
        count= count+1
    else:
        pass
        
print("DIGIT" ,count)