# 금광

t = int(input())

for _ in range(t):
    # 입력
    n, m = map(int, input().split()) # n x m 금광
    array = list(map(int, input().split())) # 각 칸의 매장량
    
    # dp 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    
    # m개의 각 열에 대하여 보텀업 다이나믹 프로그래밍 진행
    # 0열은 그대로, 1열부터 시작
    for j in range(1, m):
        for i in range(n):
            # 1. 왼쪽 위에서 오는 경우 : left_up
            if i == 0:
                left_up = -1 # 맨 위의 행이면 존재하지 않음
            else:
                left_up = dp[i - 1][j - 1]
            # 2. 왼쪽에서 오는 경우 : left
            left = dp[i][j - 1]
            # 3. 왼쪽 아래에서 오는 경우 : left_down
            if i == n - 1:
                left_down = -1 # 맨 아래의 행이면 존재하지 않음
            else:
                left_down = dp[i + 1][j - 1]
            # left_up, left, left_down 중 가장 큰 것을 선택하여 d[i][j] 갱신
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    # 결과 출력 : 마지막 열 중 가장 큰 값
    result = -1
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)