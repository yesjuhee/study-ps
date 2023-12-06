# 문자열 재정렬

import sys
input = sys.stdin.readline().rstrip

input_str = input()
alphabet_str = ""
number_sum = 0

for x in input_str:
    if x.isalpha():
        alphabet_str += x
    else:
        number_sum += int(x)


if number_sum != 0:
    print("".join(sorted(alphabet_str)) + str(number_sum))
else:
    print("".join(sorted(alphabet_str)))
