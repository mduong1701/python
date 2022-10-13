def tribo(n):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    result = [0] * (n + 1)

    # Base cases

    result[0] = 0
    result[1] = 1
    result[2] = 1

    for i in range(3, n + 1):
        result[i] = result[i-1] + result[i-2] + result[i-3]

    return result[-1]

print(tribo(4))
print(tribo(25))