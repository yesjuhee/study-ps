# 손익분기점

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if c <= b:
    x = -1
else:
    x = a//(c-b)+1

print(x)
