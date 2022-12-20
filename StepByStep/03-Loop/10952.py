# A+B - 5

import sys
while (True):
    a, b = map(int, sys.stdin.readline().split())
    if a+b > 0:
        print(a+b)
    else:
        break
