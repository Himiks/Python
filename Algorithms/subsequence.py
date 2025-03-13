def longgestSub(arr):
    arr.sort()
    res = 1
    cnt = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            continue
        if arr[i] == arr[i - 1] + 1:
            cnt+=1
        else:
            cnt = 1
        res = max(res, cnt)
        
    return res


arr = [2, 6, 1, 9, 4, 5, 3]
print(longgestSub(arr))