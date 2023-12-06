# 뱀
import sys
input = sys.stdin.readline
ROW = 0
COLUMN = 1
HEAD = 0

# 입력
n = int(input())
k = int(input())
# 사과 인덱스를 apples에 저장
apples = []
for _ in range(k):
    row, column = map(int, input().split())
    apples.append((row - 1, column - 1))
# 방향 전환 정보를 lotations 리스트에 저장
l = int(input())
lotations = []
for _ in range(l):
    x, c = input().split()
    x = int(x)
    lotations.append((x, c))


# 기본 변수 설정
steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 방향 벡터 : 동, 남, 서, 북
direction = 0                               # 뱀의 방향 : 동(0), 남(1), 서(2), 북(3)
clock = 0                                   # 시간
snake = [(0, 0)]                            # 뱀 위치 초기화


# 기본 함수 구현
# 회전
def lotate():
    global direction
    c = lotations[0][1]
    if c == "D":
        # 오른쪽(시계방향) 회전
        direction = (direction + 1) % 4
    else: 
        # 왼쪽(반시계방향) 회전
        direction = (direction - 1) % 4
    lotations.pop(0)
# 게임 오버 판단
def gameover():
    head = snake[HEAD]
    # 벽인지 판단
    if head[ROW] == -1 or head[ROW] == n:
        return True
    if head[COLUMN] == -1 or head[COLUMN] == n:
        return True
    # 자기 몸인지 판단
    if head in snake[1:]:
        return True
    # 게임이 끝나지 않음. (사과 또는 빈 칸)
    return False
# 머리를 다음 칸에 위치
def move_head():
    head = list(snake[HEAD])  # 현재 머리 위치
    head[ROW] += steps[direction][ROW]         # 머리 이동
    head[COLUMN] += steps[direction][COLUMN]   # 머리 이동
    # 이동한 머리 추가
    snake.insert(0, tuple(head))
# 꼬리를 다음 칸에 위치
def move_tail():
    snake.pop()

# 게임 시작
# 1. 회전
# 2. 머리 이동
# 3. 게임 오버 판단
# 4. tail 이동 여부(사과 여부) 판단
# 5. 시간 +1
while True:
    # 회전 여부 판단
    if lotations and lotations[0][0] == clock:
        lotate()
    
    # 머리 이동
    move_head()
    
    # 게임 오버 판단
    if gameover():
        break
    
    # 사과를 먹었는지 판단
    if snake[HEAD] in apples:
        # 사과 먹음
        apples.remove(snake[HEAD])
    else:
        # 사과 못먹음
        move_tail()
        
    clock += 1

print(clock + 1)