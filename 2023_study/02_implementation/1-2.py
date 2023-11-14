# 상하좌우 모범 답안

import sys
input = sys.stdin.readline

n = int(input())
plans = list(input().split())
x, y = 1, 1

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    # 이동 후 좌표 계산하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 이동 수행
    x, y = nx, ny

print(x, y)
