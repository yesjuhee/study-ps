# 부녀회장이 될테야

import sys
input = sys.stdin.readline

table = [[0]*14 for i in range(15)]


def get_num(k, n):
    if n == 1:
        return 1
    if k == 0:
        return n
    if table[k][n] != 0:
        return table[k][n]
    table[k][n] = table[k][n-1] + table[k-1]+n
    return table[k][n]


# 입력
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(get_num(k, n))
