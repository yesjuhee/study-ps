# 단지 번호 붙이기


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    # 현재 노드가 0 이라면
    if graph[x][y] == 1:
        # 해당 노드를 1로 바꾸고 상하좌우 연결된 0인 노드도 모두 1로 바꾸기
        graph[x][y] = 0
        house_count[complex_index] += 1
        # 상 하 좌 우 모두 확인
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True

    # 현재 노드가 1 이라면 False
    return False


# n
n = int(input())

# 얼음틀의 형태를 2차원 리스트로 저장
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


complex_count = 0   # 단지 수 카운트
house_count = [0] * 25 * 25    # 각 단지의 집 수(최대 25^2개까지 가능)
complex_index = 0   # 각 단지의 번호 -> 각 단지의 집 수를 카운트 하는 용도
for i in range(n):
    for j in range(n):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            complex_count += 1
            complex_index += 1  # 그 다음 단지를 이용하기 위해

print(complex_count)
house_count = house_count[:complex_index]
house_count.sort()
for i in range(complex_index):
    print(house_count[i])
