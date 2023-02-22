# 서로소 집합 자료구조 : 기본적인 구현 방법

# 연산 1 : 특정 원소가 속한 집합(루트 노드)를 찾아주는 연산 (find)
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 연산 2 : 두 원소가 속한 집합을 합치는 연산 (union)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 더 작은 노드를 루트 노드로 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 입력
num_node, num_edge = map(int, input().split())
parent_table = [0] * (num_node + 1)

# 부모 테이블 초기화
for i in range(1, num_node + 1):
    parent_table[i] = i;

# Union 연산을 입력받아 수행
for i in range(num_edge):
    a, b = map(int, input().split())
    union_parent(parent_table, a, b)

# 출력
print('각 원소가 속한 집합: ', end="")
for i in range(1, num_node):
    print(find_parent(parent_table, i), end=' ')

print()

print('부모 테이블: ', end="")
for i in range(1, num_node + 1):
    print(parent_table[i], end=" ")