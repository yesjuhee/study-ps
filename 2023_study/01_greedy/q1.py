# 모험가 길드
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0

# 1
result += data.count(1)
# 2
result += data.count(2) // 2
remainder = data.count(2) % 2

for i in range(3, data[-1] + 1):
    result += (remainder + data.count(i)) // i
    remainder = (remainder + data.count(i)) % i

print(result)
