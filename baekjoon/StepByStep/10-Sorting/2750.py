# 수 정렬하기

import sys
input = sys.stdin.readline

n = int(input())

number_array = []
for _ in range(n):
    number_array.append(int(input()))

number_array.sort()

print("\n".join(map(str, number_array)))
