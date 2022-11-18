# 단어 정렬

import sys
input = sys.stdin.readline

# 집합 51개를 가지는 리스트 생성
word_set_list = [set() for _ in range(51)]

n = int(input())
for _ in range(n):
    word = input().strip()
    word_len = len(word)
    word_set_list[word_len].add(word)

for word_set in word_set_list:
    if len(word_set) == 0:
        continue
    word_set = sorted(word_set)
    print('\n'.join(word_set))
