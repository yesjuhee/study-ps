# 팩토리얼

n = int(input())


def get_factorial(x):
    if x == 0:
        return 1
    return x * get_factorial(x-1)


print(get_factorial(n))
