#transpose of matrix 


X = [[1,4],
    [1 ,2]]

transpose = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for r in transpose:
   print(r)