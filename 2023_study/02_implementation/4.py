# 게임 개발

import sys
input = sys.stdin.readline().rstrip

n, m = map(int, input().split())
a, b, direction = map(int, input().split())
game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))
game_map[a][b] = 2
result = 1
# 북쪽, 동쪽, 남쪽, 서쪽
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 직진 가능한지 판단하는 함수


def zerocheck():
    result = False
    for step in steps:
        dx = a + step[0]
        dy = b + step[1]
        if game_map[dx][dy] == 0:
            result = True
            break
    return result


while True:
    if zerocheck():
        # 방향 확인용 변수
        step = direction
        while True:
            # 왼쪽 방향으로 회전
            step = (step - 1) % 4
            dx = a + steps[step][0]
            dy = b + steps[step][1]
            # 가보지 않았다면 전진
            if game_map[dx][dy] == 0:
                a = dx
                b = dy
                game_map[a][b] = 2
                result += 1
                direction = step
                break
    else:
        # 네 칸 모두 이미 가본 칸이거나 바다로 되어 있는 경우
        # 후진을 시도한다.
        step = (direction - 2) % 4
        dx = a + steps[step][0]
        dy = b + steps[step][1]
        if game_map[dx][dy] == 1:
            # 뒤 칸이 바다인 경우 종료
            break
        elif game_map[dx][dy] == 2:
            a = dx
            b = dy

print(result)
