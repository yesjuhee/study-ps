# 볼링공 고르기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

total = n * (n - 1) / 2
overlap = 0

for i in range(1, m + 1):
    count = data.count(i)
    overlap += count * (count - 1) / 2

print(total - overlap)
