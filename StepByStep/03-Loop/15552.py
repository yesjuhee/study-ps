# # 빠른 A+B
# import sys

# n = int(sys.stdin.readline())
# nlist = []
# for i in range(n):
#     nlist.append(list(map(int, sys.stdin.readline().split())))
# for numset in nlist:
#     print(numset[0]+numset[1])

# 빠른 A+B
import sys

n = int(sys.stdin.readline())
nlist = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
