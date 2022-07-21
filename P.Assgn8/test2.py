#multiplication of 2 matrices 

A = [[1,2],
    [3,4]]
    
B = [[5,6],
     [8,9]]


mul = [[0,0],
       [0,0]]

for i in range(len(A)):
      
   for j in range(len(B[0])):
       
       for k in range(len(B)):
           mul[i][j] += A[i][k] * B[k][j]


print(mul)