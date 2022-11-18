# 좌표 압축

# 리스트의 [].index()는 시간 복잡도가 n이므로 index를 n번 쓰면 시간복잡도 n^2으로 시간 초과
# 딕셔너리의 key값을 이용해 value를 찾는 연산은 시간복잡도 1

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
