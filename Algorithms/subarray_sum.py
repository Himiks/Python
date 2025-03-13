def maxSum(arr):
    res = arr[0]
    for i in range(len(arr)):
        currSum = 0
        for j in range(i, len(arr)):
            currSum = currSum + arr[j]
            
            res = max(res, currSum)
            
    return res

arr = [2, 6, -1, 9, 2, 5, 9]
print(maxSum(arr))