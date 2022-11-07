# 최소, 최대

import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
max = nlist[0]
min = nlist[0]

for num in nlist:
    if num < min:
        min = num
    elif num > max:
        max = num

print(f'{min} {max}')
