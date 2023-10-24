# 파티 - 플로이드 (시간 초과)

import sys
input = sys.stdin.readline
INF = int(1e9)

# 입력
n, m, x = map(int, input().split())

# 2차원 리스트 기본 값 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for start_node in range(1, n + 1):
    for end_node in range(1, n + 1):
        if start_node == end_node:
            graph[start_node][end_node] = 0

# 그래프 정보 입력
for _ in range(m):
    start_node, end_node, weight = map(int, input().split())
    graph[start_node][end_node] = weight


# 플로이드워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 오고 가는 시간 계산
distance = [0] * (n + 1)
for i in range(n + 1):
    cost = graph[i][x] + graph[x][i]
    if cost < INF:
        distance[i] = cost

# 출력
print(max(distance))