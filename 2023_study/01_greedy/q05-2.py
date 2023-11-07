# 볼링공 고르기 모범 답안

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

# 각 무게에 해당하는 볼링공의 개수 카운트
for x in data:
    array[x] += 1

result = 0

# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i]               # 전체에서 A가 선택할 수 있는 개수 제외
    result += array[i] * n      # (A가 선택할 수 있는 개수) * (B가 선택할 수 있는 개수)

print(result)
