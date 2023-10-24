# 골드바흐의 추측

import sys
input = sys.stdin.readline


def is_primenumber(number):
    for divisor in range(2, int(number**0.5)+1):
        if number % divisor == 0:
            return False
    return True


t = int(input())

for _ in range(t):
    n = int(input())
    partition1 = int(n/2)
    partition2 = n - partition1

    while not (is_primenumber(partition1) and is_primenumber(partition2)):
        partition1 -= 1
        partition2 += 1

    print(f'{partition1} {partition2}')
