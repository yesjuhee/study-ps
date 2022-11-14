# 수 정렬하기 2

import sys
input = sys.stdin.readline

# n 입력
n = int(input())
numberList = []

# n번 입력해서 리스트 만들기
for _ in range(n):
    numberList.append(int(input()))

# 정렬
numberList.sort()

# 출력
for x in numberList:
    print(x)
