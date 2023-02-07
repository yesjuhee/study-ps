# 병사 배치하기

# 입력
n = int(input())
array = list(map(int, input().split()))
array.reverse()

# dp 테이블
dp = [1] * n

# LIS 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))