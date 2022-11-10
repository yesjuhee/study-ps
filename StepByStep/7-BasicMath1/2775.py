# 부녀회장이 될테야

# 테이블 초기화 : size 15 x 14
dp_table = [[0]*14 for _ in range(15)]


def dp(k, n):  # DP 함수
    if k == 0:
        return n+1
    if n == 0:
        return 1
    if dp_table[k][n] != 0:
        return dp_table[k][n]

    dp_table[k][n] = dp(k, n-1) + dp(k-1, n)
    return dp_table[k][n]


# 입력 및 출력
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp(k, n-1))
