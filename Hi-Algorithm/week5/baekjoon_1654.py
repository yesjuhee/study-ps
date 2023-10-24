# 랜선 자르기

import sys
input = sys.stdin.readline

# 입력
n, k = map(int, input().split())
array = []
for _ in range(n): array.append(int(input()))

# 랜선의 최대 길이 탐색
start = 0
end = max(array)
result = 0

while (start <= end):
    mid = (start + end) // 2
    if mid == 0: mid += 1
   
    # 길이가 mid일 때 랜선의 수 계산
    lan_count = 0
    for youngsik_lan in array:
        lan_count += youngsik_lan // mid
    
    # 계산한 랜선의 개수 >= 목표 개수 -> mid 크기 늘리기
    if lan_count >= k:
        result = mid
        start = mid + 1
    # 계산한 랜선의 개수 < 목표 개수 -> mid 크기 줄이기
    elif lan_count < k:
        end = mid - 1


print(result)