# 부녀회장이 될테야

# 테이블 초기화 : size 15 x 14
dp_table = [[0]*14 for _ in range(15)]

# DP 함수


# 입력 및 출력
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp_table(k, n-1))
