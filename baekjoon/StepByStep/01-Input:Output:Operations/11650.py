# 좌표 정렬하기

# 입력
n = int(input())
dots = []
for i in range(n):
    dot = list(map(int, input().split()))
    dots.append(dot)

# x 기준으로 먼저 정렬-> if x가 같으면 y를 기준으로 다시 정렬
dots.sort()

# 출력
for i in range(n):
    print(f'{dots[i][0]} {dots[i][1]}')
