from collections import deque


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


# 그래프의 연결 정보를 2차원 리스트로 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드의 방문 여부를 1차원 리스트로 표현
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
