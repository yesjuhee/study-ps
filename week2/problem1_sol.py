# 1이 될 때까지

# 입력
n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k  # n이하의 n과 가장 가까운 k의 배수
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)
