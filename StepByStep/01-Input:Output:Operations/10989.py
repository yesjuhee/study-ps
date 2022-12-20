# 수 정렬하기 3

# 입력
import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*10001

for i in range(n):
    arr[int(input())] += 1

# 출력
for i in range(10001):       # i인 것은 몇개?
    for j in range(arr[i]):  # arr[i]의 원소 수 만큼
        print(i)
