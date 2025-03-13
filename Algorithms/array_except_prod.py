def product(arr):
    n = len(arr)
    res = [1] * n

    
    for i in range(n):
        for j in range(n):
            if i != j:
                res[i] *= arr[j]
    return res


arr = [2, 0, 4, 9, 19, 5, 2]
res = product(arr)
print(res)