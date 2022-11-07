# OX 퀴즈

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):  # n번 반복
    # 입력 및 초기화
    oxlist = input()
    score = 0
    sum = 0

    # 해당 해차 점수 계산
    for ox in oxlist:
        if ox == 'O':
            score += 1
        else:
            score = 0
        sum += score

    # 점수 출력
    print(sum)
