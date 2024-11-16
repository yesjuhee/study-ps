# 치킨 배달
import sys
input = sys.stdin.readline

# 하나의 집의 치킨 거리를 구한다
def get_chicken_path(chickens, house):
    pathes = []
    for chicken in chickens:
        pathes.append(abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))
    return min(pathes)

# 도시의 치킨 거리를 구한다
def get_city_chicken(city, chickens):
    result = 0
    for x in range(n):
        for y in range(n):
            if city[x][y] == 1:
                # 집에 대해서 치킨 거리 구하기
                result += get_chicken_path(chickens, (x, y))
    return result

# 입력 받기
n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

# 치킨집 좌표 저장
chickens = []
for x in range(n):
    for y in range(n):
        if city[x][y] == 2:
            chickens.append((x, y))

# 치킨집이 m 개라면 바로 정답 구하기
if len(chickens) == m:
    print(get_city_chicken(city, chickens))
# 치킨 집 m 개 남기는 모든 경우의 수 탐색
else:
    # 각각의 경우에 대해 도시의 치킨 거리 계산
    new_chickens = []
    indexes = [x for x in range(m)]
    