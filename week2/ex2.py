# 상하좌우

x, y = 1, 1

# 입력
n = int(input())
plan = list(input().split())

for direction in plan:
    if direction == 'R' and y < n:
        y += 1
    elif direction == 'L' and y > 1:
        y -= 1
    elif direction == 'U' and x > 1:
        x -= 1
    elif direction == 'D' and x < n:
        x += 1

print(x, y)