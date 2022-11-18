# 좌표 정렬하기 2

# 입력
n = int(input())
dots = []
for i in range(n):
    x, y = map(int, input().split())
    dots.append([y, x])

dots.sort()

# 출력
for i in range(n):
    print(f'{dots[i][1]} {dots[i][0]}')
