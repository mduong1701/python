def nonConstructibleChange(coins):
    # if empty array, return 1
    if len(coins) == 0:
        return 1

    # Sort the array
    coins.sort()

    # Current change being created
    current_change = 0
    # Loop through the array
    for coin in coins:
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin
    return current_change + 1
    
arr1 = []
arr2 = [1,2,5]
arr3 = [5,7,1,1,2,3,22]

print(nonConstructibleChange(arr1))
print(nonConstructibleChange(arr2))
print(nonConstructibleChange(arr3))