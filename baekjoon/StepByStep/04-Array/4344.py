# 평균은 넘겠지

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    score_list = list(map(int, input().split()))
    del score_list[0]
    # 평균 계산
    mean = sum(score_list)/len(score_list)
    # 비율 계산
    count = 0
    for score in score_list:
        if score > mean:
            count += 1
    # 출력
    print(f'{count/len(score_list)*100:.3f}%')
