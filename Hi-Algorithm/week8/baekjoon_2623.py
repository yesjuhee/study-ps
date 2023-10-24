# 음악프로그램

from collections import deque
import sys
input = sys.stdin.readline

# 입력 및 초기화
num_node, m = map(int, input().split())

indegree = [0] * (num_node + 1)             # 각 노드의 진입 차수
graph = [[] for i in range(num_node + 1)]   # 각 노드의 간선 연결 정보 (graph[a][b] : a->b 연결)

# 보조 pd의 정보를 바탕으로 그래프 입력
for _ in range(m):
    order = list(map(int, input().split()))
    for i in range(1, order[0]):
        graph[order[i]].append(order[i + 1])
        indegree[order[i + 1]] += 1



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

# 출력
# 위상 정렬이 가능한지 확인
if len(result) == num_node:
    for node in result:
        print(node)
else:
    print(0)
