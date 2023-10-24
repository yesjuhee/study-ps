# 나머지

# 입력
import sys
a, b, c = map(int, sys.stdin.readline().split())

# 출력
print((a+b) % c)
print(((a % c)+(b % c)) % c)
print((a*b) % c)
print(((a % c)*(b % c)) % c)
