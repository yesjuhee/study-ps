# 베르트랑 공준

import sys
input = sys.stdin.readline


def get_primenumber(n):
    prime_tf_list = [False]*2 + [True]*(2*n-1)
    for x in range(2, int((2*n)**0.5)+1):
        if prime_tf_list[x] == True:
            step = 2
            while step * x <= 2 * n:
                prime_tf_list[step * x] = False
                step += 1

    count = 0
    for index in range(n+1, 2*n+1):
        if prime_tf_list[index]:
            count += 1

    return count


while True:
    n = int(input())
    if n == 0:
        break
    print(get_primenumber(n))
