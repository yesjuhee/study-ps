# 킹, 퀸, 룩, 비숍, 나이트, 폰

# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
import sys
piece = [1, 1, 2, 2, 2, 8]

# 입력
imcomplete = list(map(int, sys.stdin.readline().split()))
for a, b in zip(piece, imcomplete):
    print(a-b, end=' ')
