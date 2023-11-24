# 왕실의 나이트

import sys
input = sys.stdin.readline

position = input()
x = ord(position[0]) - ord("a") + 1
y = int(position[1])

moves = [[-2, -1], [-2, +1], [+2, -1], [+2, +1],
         [-1, -2], [-1, +2], [+1, -2], [+1, +2]]

result = 0

for move in moves:
    dx = x + move[0]
    dy = y + move[1]
    if 1 <= dx <= 8 and 1 <= dy <= 8:
        result += 1

print(result)
