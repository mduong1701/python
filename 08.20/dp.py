# def fibonacci(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n >=2:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(7))

# ----------------------------------------------------

def fibo(n):
    arr = [0] * n
    arr[0], arr[1] = 1, 1
    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[i]

print(fibo(8))
