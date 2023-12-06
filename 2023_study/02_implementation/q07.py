# 럭키 스트레이트

import sys
input = sys.stdin.readline().rstrip

n = input()
n_len = len(n)
right = 0
left = 0

for i in range(n_len // 2):
    right += int(n[i])
    left += int(n[n_len - i - 1])

if right == left:
    print("LUCKY")
else:
    print("READY")
