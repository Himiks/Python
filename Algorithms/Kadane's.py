def maxSum(arr):
    res = arr[0]
    maxEnd= arr[0]
    
    
    for i in range(1, len(arr)):
        maxEnd = max(maxEnd + arr[i], arr[i])
        res = max(res, maxEnd)
    return res

arr = [2, 3, 7, 3, -1, 2, 3]
print(maxSum(arr))