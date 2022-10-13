def min_cost(arr):
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return arr[0]

    if len(arr) == 2:
        return min(arr[0], arr[1])

    result = [0] * (len(arr) + 1)

    # base cases
    result[0] = 0
    result[1] = 0

    for i in range(2, len(result)):
        result[i] = min(result[i-1] + arr[i-1], result[i-2] + arr[i-2])
    
    return result[-1]

print(min_cost([10,15,20]))
print(min_cost([1,100,1,1,1,100,1,1,100,1]))