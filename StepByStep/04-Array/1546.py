# 평균

import sys
input = sys.stdin.readline

n = int(input())

slist = list(map(int, input().split()))
max_score = max(slist)
for i in range(n):
    slist[i] = slist[i]/max_score*100

print(sum(slist)/len(slist))
