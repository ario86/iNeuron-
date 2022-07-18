#Monotonic array

arr=[1,2,3,4,5,6,7,8,9,10]
def monotonic(arr):
    increasing = False
    if(arr[0]>arr[1]):
        increasing = False
        
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1] and increasing or arr[i+1]>arr[i] and not increasing):
            return True
        else:
            return False
        
print(monotonic(arr))