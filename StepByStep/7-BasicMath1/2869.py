# 달팽이는 올라가고 싶다

import sys
input = sys.stdin.readline

up, down, top = map(int, input().split())
count = up-down
if (top-up) % count == 0:  # 나누어 떨어짐
    print((top-up)//count + 1)
else:
    print((top-up)//count + 2)
