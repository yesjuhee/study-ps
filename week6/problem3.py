# # 효율적인 화폐 구성

# # 입력
# n, m = map(int, input().split())
# array = []
# for i in range(n):
#     array.append(int(input()))

# # dp 테이블
# d = [10001] * (m + 1)

# # 다이나믹 프로그래밍 보텀업
# d[0] = 0
# for i in range(n):
#     for j in range(array[i], m + 1):
#         if d[j - array[i]] != 10001:
#             d[j] = min(d[j], d[j - array[i]] + 1)

# # 출력
# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])

# 효율적인 화폐 구성 2

# 입력
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

# dp 테이블
d = [10001] * (m + 1)
d[0] = 0

# 다이나믹 프로그래밍 진행 (보텀업)
for i in range(1, m + 1):
    for k in array:
        if i - k >= 0:
            d[i] = min(d[i], d[i - k] + 1)

if d[m] > 10000:
    print(-1)
else:
    print(d[m])