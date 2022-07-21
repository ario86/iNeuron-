#sum of 2 matrices 

A = [[1,2],
    [3,4]]
    
B = [[5,6],
     [8,9]]


sum = [[0,0],
       [0,0]]

for i in range(len(A)):  

    for j in range(len(A[0])):
        sum[i][j] = A[i][j] + B[i][j]
 

    print(sum)