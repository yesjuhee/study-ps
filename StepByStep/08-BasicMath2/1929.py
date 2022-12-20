# 소수 구하기

# 소수

# 입력
import sys
input = sys.stdin.readline
m, n = map(int, input().split())

# n이하의 배열
tf_array = [True]*(n+1)
tf_array[0] = False
tf_array[1] = False

# 소수 여부 판단해서 리스트 반환 (에라토스테네스의 채)
for x in range(2, int(n**0.5 + 1)):
    if tf_array[x] == True:
        step = 2
        while x * step <= n:
            tf_array[x*step] = False
            step += 1

prime_list = [x for x in range(m, n+1) if tf_array[x] == True]

for x in prime_list:
    print(x)
