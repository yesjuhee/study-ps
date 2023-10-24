# 부녀회장이 될테야

# dp 테이블
dp = [[0]*15 for _ in range(15)]
# 0층 초기화
dp[0] = [x for x in range(0, 15)]
# 1호 초기화
for i in range(15):
    dp[i][1] = 1

for tc in range(int(input())):
    # 입력
    k = int(input())
    n = int(input())
    # k층 n호까지 다이나믹 프로그래밍 실행
    for i in range(1, k + 1):
        for j in range(2, n + 1):
            dp[i][j] = dp[i][j-1] + dp[i - 1][j]
    # 출력
    print(dp[k][n])
