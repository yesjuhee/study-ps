# 피보나치 수 5

n = int(input())


def get_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return get_fibonacci(n-1) + get_fibonacci(n-2)


print(get_fibonacci(n))
