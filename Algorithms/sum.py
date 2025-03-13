def twoSum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return True
    return False


arr = [3, -1, 2, 8, 1]
target = 5

if twoSum(arr, target):
    print("true")
else:
    print("false")