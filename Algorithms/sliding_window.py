def slicing_window(arr, k):
    n = len(arr)
    res = []

    for i in range(0, n - k + 1):
        max = arr[i]
        for j in range(1, k):
            if arr[i + j] > max:
                max = arr[i + j]
        res.append(max)

    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 3
    res = slicing_window(arr, k)
    for maxV in res:
        print(maxV, end=" ")
