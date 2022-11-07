# ACM 호텔

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    # N = aH + b
    if N % H == 0:
        print(f'{H}{N//H:02d}')
    else:
        print(f'{N%H}{N//H+1:02d}')
