# DFS와 BFS
from collections import deque

# 1. n, m, v 입력
n, m, v = map(int, input().split())


# 2. 간선 입력 & 그래프 생성
# 2차원 리스트 초기화
graph = [[] for _ in range(n + 1)]  # n + 1개의 행을 가지는 2차원 리스트
# m개의 간선 정보 입력
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
# 입력된 정보 정렬
for row in graph:
    row.sort()


# 3. BFS 수행 결과 출력
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * (n+1)
# 정의된 DFS 함수 호출
dfs(graph, v, visited)
print()

# 4. BFS 수행 결과 출력


def bfs(graph, start, visited):
    # 방문할 노드를 저장할 큐
    queue = deque([start])
    # 첫 번째 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 아래의 과정 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력(방문)
        v = queue.popleft()
        print(v, end=' ')
        # 연결된 노드 중 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드의 방문 여부를 1차원 리스트로 표현
visited = [False] * (n+1)

# 정의된 BFS 함수 호출
bfs(graph, v, visited)
print()
