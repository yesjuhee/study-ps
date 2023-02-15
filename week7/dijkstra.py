# 다익스트라 알고리즘 : 간단한 구현 방법
import sys
input = sys.stdin.readline
INF = int(1e9) # 1 * 10^9 (10억억

# 입력 1
node_num, edge_num = map(int, input().split())
start_node = int(input())

graph = [[] for i in range(node_num + 1)] # 간접 리스트, 각 행은 각 노드의 연결을 의미함
visited = [False] * (node_num + 1)        # 노드의 방문 여부를 체크하는 리스트
distance = [INF] * (node_num + 1)         # 최단 거리 테이블

# 입력 2 - 간선 정보
for _ in range(edge_num):
    a, b, c = map(int, input().split())  # a노드에서 b노드까지의 간선 비용이 c
    graph[a].append((b, c))              # 간접 리스트에 튜플 자료형을 이용해 저장


# 방문하지 않은 노드 중에서, 계산된 거리가 가장 짧은 노드의 번호를 반환하는 함수
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, node_num+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


# 다익스트라 함수
def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0         # 시작 노드까지의 거리 0
    visited[start] = True       # 시작 노드 방문 처리
    for j in graph[start]:      # 시작 노드와 연결된 모든 노드의 거리 값 갱신
        # j[0] : start에 연결된 노드 번호
        # j[1] : 해당 번호와 start 노드 사이의 거리
        distance[j[0]] = j[1]
    # 나머지 노드에 대해 다익스트라 알고리즘 반복 수행
    for i in range(node_num - 1): 
        # 계산된 거리가 가장 짧은 노드 선택
        now = get_smallest_node()
        visited[now] = True
        # now 노드와 연결된 모든 노드의 연결값 갱신 or 확인
        for j in graph[now]:
            # j[0] : now에 연결된 노드 번호
            # j[1] : 해당 번호와 now 노드 사이의 거리
            cost = distance[now] + j[1] # now 노드를 거쳐가는 경우의 거리
            if cost < distance[j[0]]:
                distance[j[0]] = cost   # 기존 값보다 작은 경로라면 갱신
              

dijkstra(start_node)

# start 노드로부터 모든 노드로까지의 최단 거리 출력
for i in range(1, node_num + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])