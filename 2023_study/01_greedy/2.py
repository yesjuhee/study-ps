# 숫자 카드 게임
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data1 = []
data2 = []

for i in range(N):
    data1 = list(map(int, input().split()))
    data2.append(min(data1))

print(max(data2))
