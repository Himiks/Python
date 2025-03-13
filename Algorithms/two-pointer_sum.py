def twoSum(arr, target):
    arr.sort()
    
    left, right = 0, len(arr) -1
    
    while left < right:
        sum = arr[left] + arr[right]
        
        if sum == target:
            return True
        elif sum < target:
            left+=1
        else:
            right -= 1
    return False

arr = [3, -1, 2, 8, 1]
target = 5

if twoSum(arr, target):
    print("true")
else:
    print("false")