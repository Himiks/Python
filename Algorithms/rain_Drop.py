def maxWater(arr):
    res = 0
    for i in range(1, len(arr) - 1):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
            

        right = arr[i]
        for j in range(i + 1, len(arr)):
            right = max(right, arr[j])
           

        
        print("Left: ", left)
        print("Right: ", right)
        print("Res: ", res)
        res += min(left, right) - arr[i]
        print("Res: ", res)
        
    return res


arr = [2, 1, 5, 3, 1, 0, 4]
print(maxWater(arr))
