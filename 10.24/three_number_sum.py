def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            if array[i] + array[left] + array[right] == targetSum:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif array[i] + array[left] + array[right] > targetSum:
                right -= 1
            else:
                left += 1
    return result

print(threeNumberSum([12,3,1,2,-6,5,-8,6], 0))