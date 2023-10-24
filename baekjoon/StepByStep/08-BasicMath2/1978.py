# 소수 찾기

import sys
input = sys.stdin.readline

_ = int(input())

array = list(map(int, input().split()))


def is_primenumber(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


count = 0
for x in array:
    if x != 1 and is_primenumber(x):
        count += 1
print(count)
