def min_moves(array):
    isSorted = False
    counter = 0
    result = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                result += 1
                isSorted = False
        counter += 1
    return result

print(min_moves([5,4,3,2,1]))
