#duplicate characters

a = "hello"

duplicate = []
for char in a:

   if a.count(char) > 1:
   
    if char not in a:
        duplicate.append(char)
print(*a)