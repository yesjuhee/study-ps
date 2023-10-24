# 예산
import sys
input = sys.stdin.readline

# 입력
n = int(input())
array = list(map(int, input().split()))
total = int(input())

# 모두 배정 가능한지 확인
if sum(array) <= total:
    print(max(array))
    exit()

# 이진 탐색으로 상한액 찾기
start = 1
end = max(array)
result = 0

while (start <= end):
    mid = (start + end) // 2
   
    # 상한액이 mid일 때 총 예산 계산
    budget = 0
    for money in array:
        if money <= mid:
            budget += money
        else:
            budget += mid
    
    # 계산한 예산이 총 예산을 넘어감 -> mid 값을 줄여야 함
    if budget > total:
        end = mid - 1
    # 계산한 예산이 총 예산보다 작음 -> mid값을 키워야 함
    elif budget <= total:
        result = mid
        start = mid + 1

print(result)