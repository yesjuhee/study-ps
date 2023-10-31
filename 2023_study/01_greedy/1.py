# 큰 수의 법칙
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)
sum = 0

while M > K:
    sum += K * array[0] + array[1]
    M -= (K + 1)
    
sum += M * array[0]

print(sum)
        