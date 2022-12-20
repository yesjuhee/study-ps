# 최댓값

import sys
input = sys.stdin.readline

row = 1
column = 1
total_max = 0

for i in range(1, 10):
    row_array = list(map(int, input().split()))
    max_in_array = max(row_array)
    if max_in_array > total_max:
        row = i
        column = row_array.index(max_in_array) + 1
        total_max = max_in_array

print(total_max)
print(f'{row} {column}')
