# X보다 작은 수

import sys
input = sys.stdin.readline
# n과 x 입력
n, x = map(int, input().split())

# n개 입력
nlist = list(map(int, input().split()))

for num in nlist:
    if num < x:
        print(num, end=' ')
