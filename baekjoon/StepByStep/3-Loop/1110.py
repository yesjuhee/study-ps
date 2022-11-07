# 더하기 사이클

origin = int(input())
cur = origin
count = 0

while (True):
    units = cur % 10
    tens = cur//10
    cur = units*10 + (tens+units) % 10
    count += 1
    if cur == origin:
        print(count)
        break
