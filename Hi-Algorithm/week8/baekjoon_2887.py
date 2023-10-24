# 행성 터널

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 더 작은 노드를 루트 노드로 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 행성 개수 입력
num_node = int(input())

# 행성 좌표 입력
points = [[]]
for _ in range(num_node):
    points.append(list(map(int, input().split())))

# 부모 테이블 초기화
parent_table = [0] * (num_node+ 1)
for i in range(1, num_node + 1):
    parent_table[i] = i

# 모든 간선 계산
edges = []
num_edge = num_node * (num_node-1) / 2
for a in range(1, num_node):
    for b in range(a+1, num_node+1):
        a_point = points[a]
        b_point = points[b]
        cost = min([abs(a_point[0]-b_point[0]), abs(a_point[1]-b_point[1]), abs(a_point[2]-b_point[2])])
        edges.append((cost, a, b))

# 간선을 비용 오름차순으로 정렬
edges.sort()

result = 0
# 크루스칼 알고리즘
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우
    if find_parent(parent_table, a) != find_parent(parent_table, b):
        union_parent(parent_table, a, b)
        # 신장 트리의 간선으로 선택(최종 비용에 포함)
        result += cost

print(result)