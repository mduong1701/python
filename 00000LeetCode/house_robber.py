def rob(arr):
    if len(arr) == 0:
        return 0
    
    if len(arr) == 1:
        return arr[0]

    rob_arr = [0] * len(arr)

    # Base case
    rob_arr[0] = arr[0]
    rob_arr[1] = max(arr[0], arr[1])

    for i in range(2, len(rob_arr)):
        rob_arr[i] = max(rob_arr[i-1], rob_arr[i-2] + arr[i])

    return rob_arr[-1]

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))

