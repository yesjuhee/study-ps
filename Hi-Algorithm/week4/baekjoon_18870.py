# 좌표 압축

import sys
input = sys.stdin.readline

n = int(input())
number_list = list(map(int, input().split()))

number_set = set(number_list)
number_set = sorted(number_set)
number_dict = {}
for i in range(len(number_set)):
    number_dict[number_set[i]] = i

for x in number_list:
    print(number_dict[x])

# for x in number_list:
#     print(number_set.index(x), end=' ')
# O(n^2)으로 시간 초과 발생
