# 1. Countdown
def countDown(startNum):
    listCountDown = []
    for i in range(startNum, -1, -1):
        listCountDown.append(i)
    return listCountDown
print(countDown(10))

# 2. Print and Return
def printReturn(ls):
    print(ls[0])
    return ls[1]
printReturn([5, 10])
print(printReturn([5, 10]))

# 3. First Plus Length
def first_plus_length(ls):
    return ls[0] + len(ls)
print(first_plus_length([10, 2, 3, 4, 5]))

# 4. Values Greater than Second
def values_greater_than_second(ls):
    if len(ls) < 2:
        return False
    new_ls = []
    count = 0
    second_value = ls[1]
    for i in range(len(ls)):
        if ls[i] > second_value:
            count += 1
            new_ls.append(ls[i])
    print(count)
    return new_ls
print(values_greater_than_second([1,2,3,4,5,6]))
print(values_greater_than_second([10]))

# 5. This Length, That Value
def length_and_value(size, value):
    ls = []
    for i in range(size):
        ls.append(value)
    return ls
print(length_and_value(5, 8))

