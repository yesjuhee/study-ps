# 곱하기 혹은 더하기

import sys
input = sys.stdin.readline

S = input()

a = int(S[0])

for i in range(1, len(S)-1):
    b = int(S[i])
    if (min(a, b) <= 1):
        a += b
    else:
        a *= b

print(a)
