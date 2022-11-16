# 행렬 덧셈

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

for _ in range(n):
    tmp = list(map(int, input().split()))
    b.append(tmp)

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] += b[i][j]

for row in a:
    print(*row)
