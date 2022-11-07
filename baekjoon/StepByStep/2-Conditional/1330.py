# 두 수 비교하기

# 입력
import sys
a, b = map(int, sys.stdin.readline().split())

# 비교 및 출력
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print("==")
