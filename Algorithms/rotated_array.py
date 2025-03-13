def Min(arr):
    res = arr[0]
    
    for i in range (1, len(arr)):
        res = min(res, arr[i])
        
    return res

arr = [100, 650, 1, 44, 2, 4]
print(Min(arr))