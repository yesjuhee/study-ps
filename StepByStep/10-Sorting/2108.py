# 통계학

import sys
input = sys.stdin.readline

n = int(input())

number_list = []
for _ in range(n):
    number_list.append(int(input()))

# 산술평균
print(round(sum(number_list)/len(number_list)))

# 중앙값
number_list.sort()
print(number_list[int(len(number_list)/2)])

# 최빈값
# number_set = set(number_list)
# counting_list = []
# for x in number_set:
#     counting_list.append(number_list.count(x))
# max_count = max(counting_list)
# mode_list = [x for x in number_set if number_list.count(x) == max_count]
# if len(mode_list) != 1:
#     print(mode_list[1])
# else:
#     print(mode_list[0])
counting_dict = {}
for x in number_list:
    if x not in counting_dict:
        counting_dict[x] = 1
    else:
        counting_dict[x] += 1

max_count = max(counting_dict.values())

mode_list = [key for key in counting_dict if counting_dict[key] == max_count]
if len(mode_list) != 1:
    print(mode_list[1])
else:
    print(mode_list[0])


# 범위
print(max(number_list)-min(number_list))
