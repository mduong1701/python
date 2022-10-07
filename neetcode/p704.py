def search(arr, target):
    left = 0
    right = len(arr) - 1
    while(left <= right):
        middle = (left + right) // 2
        if (arr[middle] == target):
            return middle
        elif (arr[middle] > target):
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(search([-1,0,3,5,9,12], 9))
print(search([-1,0,3,5,9,12], 2))
