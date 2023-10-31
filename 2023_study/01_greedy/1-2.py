# 큰 수의 법칙 - 모범 답안 적용
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
first = array[N - 1]
second = array[N - 2]

# 가장 큰 수가 더해지는 횟수
count = int(M / (K + 1)) * K
count += M % (K + 1)

sum = 0
sum += count * first
sum += (M - count) * second

print(sum)
