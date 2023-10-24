# 최댓값

max = 0
index = 0

for i in range(9):
    num = int(input())
    if num > max:
        max = num
        index = i+1

print(max)
print(index)
