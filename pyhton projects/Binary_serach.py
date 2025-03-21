

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while start <= end:
        print(f"Steps: {steps} : {list[start:end+1]}")
        steps += 1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        elif element > list[middle]:
            start = middle + 1

    return -1



my_list = [1,2,3,4,5,6,7,8,9]
target = 2
print(binary_search(my_list, target))