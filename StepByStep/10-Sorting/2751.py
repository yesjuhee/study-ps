# 수 정렬하기 2

import sys
input = sys.stdin.readline

n = int(input())
numberList = []

for _ in range(n):
    numberList.append(int(input()))

numberList.sort()

for x in numberList:
    print(x)
