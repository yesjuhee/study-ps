# 크루스칼 알고리즘

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

# 입력 및 초기화
num_node, num_edge = map(int, input().split())

parent_table = [0] * (num_node+ 1)  # 부모 테이블
edges = []                          # 간선 리스트
result = 0                          # 최종 비용
for i in range(1, num_node + 1):
    parent_table[i] = i

for _ in range(num_edge):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용 오름차순으로 정렬
edges.sort()

# 크루스칼 알고리즘
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우
    if find_parent(parent_table, a) != find_parent(parent_table, b):
        union_parent(parent_table, a, b)
        # 신장 트리의 간선으로 선택(최종 비용에 포함)
        result += cost

print(result)