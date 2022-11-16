# 색종이

import sys
input = sys.stdin.readline

paper = [[False]*100 for _ in range(100)]

n = int(input())

for _ in range(n):
    x0, y0 = map(int, input().split())
    for x in range(x0, x0 + 10):
        paper[x][y0:y0+10] = [True]*10

count = 0
for row in paper:
    count += row.count(True)

print(count)
