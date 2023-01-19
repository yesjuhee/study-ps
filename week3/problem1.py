# 음료수 얼려 먹기 문제

# dfs를 이용해 주변의 0인 노드를 탐색하고 방문하는 함수
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드가 0 이라면
    if graph[x][y] == 0:
        # 해당 노드를 1로 바꾸고 상하좌우 연결된 0인 노드도 모두 1로 바꾸기
        graph[x][y] = 1
        # 상 하 좌 우 모두 확인
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    
    # 현재 노드가 1 이라면 False 
    return False

# n, m 입력
n, m = map(int, input().split())

# 얼음틀의 형태를 2차원 리스트로 저장
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드를 탐색하면서
# 해당 노드가 0 이라면 -> 연결된 0 노드를 모두 1로 바꾸고 result += 1
# 해당 노드가 1 이라면 -> pass
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)