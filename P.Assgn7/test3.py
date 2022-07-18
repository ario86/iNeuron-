arr = [1, 2, 3, 4, 5]
rotate = 1

def rightArrRotate(arr, rotate):
    for i in range(0, rotate):
        temp=arr[len(arr)-1]
        for j in range(len(arr)-1,0,-1):
            arr[j] = arr[j-1]
        arr[0] = temp
        
    return arr

def printArr(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=' ')
        
rotated_arr = rightArrRotate(arr, rotate)
print(rotated_arr)
            
    