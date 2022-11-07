# 부녀회장이 될테야

import sys
input = sys.stdin.readline


def get_num(k, n):
    if k != 0 and n != 1:
        return get_num(k, n-1)+get_num(k-1, n)
    elif n == 1:
        return 1
    else:
        return n


# 입력
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(get_num(k, n))
