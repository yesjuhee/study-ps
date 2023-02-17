# 플로이드
import sys
input = sys.stdin.readline
INF = int(1e9)
# 입력
n = int(input())
m = int(input())

# 2차원 리스트 기본 값 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for start_node in range(1, n + 1):
    for end_node in range(1, n + 1):
        if start_node == end_node:
            graph[start_node][end_node] = 0

# 그래프 정보 입력
for _ in range(m):
    start_node, end_node, weight = map(int, input().split())
    if graph[start_node][end_node] > weight:
        graph[start_node][end_node] = weight   

# 플로이드워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("0", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()