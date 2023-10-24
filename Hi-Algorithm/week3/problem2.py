# 미로 탈출

from collections import deque

# n, m 입력
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 방향벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    # 현재 위치에서 상하좌우로 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 미로 찾기 공간을 벗어난 경우 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 벽인 경우 무시
        if graph[nx][ny] == 0:
            continue
        # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

# 가장 오른쪽 아래의 최단 거리 출력
print(graph[n-1][m-1])
