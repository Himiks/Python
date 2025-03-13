def product(arr):
    zero = 0
    idx = -1
    prod = 1
    
    for i in range(len(arr)):
        if arr[i] == 0:
            zero +=1
            idx = i
        else:
            prod *=arr[i]
    res = [0] * len(arr)
    
    
    if zero == 0:
        for i in range(len(arr)):
            res[i] = prod // arr[i]
    elif zero == 1:
        res[idx] = prod
        
    return res
        
        
        
arr = [2, 0, -1, 9, 19, 5, 2]
res = product(arr)
print(res)