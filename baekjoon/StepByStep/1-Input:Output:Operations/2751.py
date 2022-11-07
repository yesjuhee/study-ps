# 수 정렬하기 2

# 입력
import sys
n = int(input())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

# 정렬 (삽입 정렬)
for end in range(1, n):
    for i in range(end, 0, -1):
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
        else:
            break

# 출력
for i in arr:
    print(i)


# 결과 --> 시간초과
