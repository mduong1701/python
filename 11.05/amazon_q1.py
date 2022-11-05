import math

def max_quality(array, channels):
    array.sort()
    quality = 0
    max_value_index = len(array) - 1

    while channels > 1:
        quality += array[max_value_index]
        max_value_index -= 1
        channels -= 1

    if max_value_index % 2 == 0:
        quality += array[max_value_index // 2]
    else: 
        quality += math.ceil((array[max_value_index // 2] + array[(max_value_index // 2) + 1]) / 2)

    return quality

print(max_quality([2,2,1,5,3], 2))
print(max_quality([1,2,3,4,5], 2))
print(max_quality([89,48,14], 3))