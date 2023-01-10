# 거스름돈

coins = [500, 100, 50, 10, 5, 1]  # 거스름돈 리스트
count = 0

price = int(input())
change = 1000 - price

for coin in coins:
    while change >= coin:
        change -= coin
        count += 1

print(count)