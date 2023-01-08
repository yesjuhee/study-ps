# 1이 될 때까지

# 입력
n, k = map(int, input().split())

result = 0

while n > 1:
    if n % k == 0: 
        # n이 k로 나누어 떨어지는 경우
        n //= k
        result += 1
    else:
        # n이 k로 나누어 떨어지지 않는 경우
        n -= 1
        result += 1

print(result)