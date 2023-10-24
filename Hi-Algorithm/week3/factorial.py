# 반복적으로 구현
def fectorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)
