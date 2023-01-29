# 떡볶이 떡 만들기

import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
food = list(map(int, input().split()))

food.sort(reverse = True)


# 절단

for knife in range(food[0]-1, 0, -1):
    product = 0
    for i in range(n):
        if food[i] <= knife:
            break
        product += food[i] - knife
    if product >= m:
        break

print(knife)
