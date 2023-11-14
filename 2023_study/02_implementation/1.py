# 상하좌우

import sys
input = sys.stdin.readline

n = int(input())
data = list(input().split())
point = [1, 1]

for move in data:
    if move == "R" and point[0] < n:
        point[1] += 1
    elif move == "L" and point[0] >= 2:
        point[1] -= 1
    elif move == "U" and point[0] >= 2:
        point[0] -= 1
    elif move == "D" and point[1] < n:
        point[0] += 1

print(point)
