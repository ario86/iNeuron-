#2


a = input("enter value for row, col: ")
row, col = a.split(",")
row = int(row)
col = int(col)

grid =[]
for x in range(row):
    row = []

    
    for y in range(col):
        row.append(x*y)
        
    
    grid.append(row)

print(grid)