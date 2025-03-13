def binary_search(arr, left, right, target):
    print(left)
    while left <= right:
        mid = left + (right - left) // 2 # -1, 1, 2, 3, 8
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False



def twoSum(arr, target):
    arr.sort()
    for i in range(len(arr)):
        complement = target - arr[i] 
        
        if binary_search(arr, i + 1, len(arr) - 1, complement):
            return True
        


arr = [3, -1, 2, 8, 1] 
target = 5

if twoSum(arr, target):
    print("true")
else:
    print("false")