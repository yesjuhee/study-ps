# 단어 정렬
import sys
input = sys.stdin.readline

# 집합 51개를 가지는 리스트 생성
word_set_list = [set() for _ in range(51)]

# 입력
n = int(input())
for _ in range(n):
    word = input().rstrip()
    word_set_list[len(word)].add(word)

# 정렬 & 출력
for word_set in word_set_list:
    if len(word_set) == 0:
        continue
    word_set = sorted(word_set)
    print('\n'.join(word_set))

# # 윤주 풀이
# from sys import stdin
# n = int(input())

# str = []
# for _ in range(n):
#     str.append(stdin.readline().rstrip())

# str = list(set(str))
# str.sort(key = lambda x:(len(x),x))
# for s in str: print(s)
