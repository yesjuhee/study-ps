# 수 정렬하기 2

# 입력
import sys
n = int(input())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

# 정렬 (삽입 정렬)
arr.sort()

# 출력
for i in arr:
    print(i)
