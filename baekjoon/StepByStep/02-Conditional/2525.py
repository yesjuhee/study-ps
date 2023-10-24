# 오븐 시계

# 입력
import sys
h, m = map(int, sys.stdin.readline().split())
cook = int(input())

total = h*60 + m + cook
h = total//60 % 24
m = total % 60
print(f'{h} {m}')
