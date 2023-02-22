# 위상 정렬 알고리즘

from collections import deque

# 입력 및 초기화
num_node, num_edge = map(int, input().split())

indegree = [0] * (num_node + 1)             # 각 노드의 진입 차수
graph = [[] for i in range(num_node + 1)]   # 각 노드의 간선 연결 정보 (graph[a][b] : a->b 연결)
for _ in range(num_edge):
    a, b = map(int, input().split())
    graph[a].append(b)  # a->b 연결
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []     # 알고리즘 수행 결과
    q = deque()

    # 큐 초기화 : 진입 차수가 0인 노드
    for i in range(1, num_node + 1):
        if indegree[i] == 0:
            q.append(i)

    # q가 빌 때까지
    while q:
        now = q.popleft()   # 큐에서 꺼낸 노드
        result.append(now)
        # now에서 나오는 간선 제거
        for i in graph[now]:
            indegree[i] -= 1
            # 진입차수가 0이 됐다면 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
        
        # 결과 출력
        for node in result:
            print(node, end=' ')

topoloty_sort()

