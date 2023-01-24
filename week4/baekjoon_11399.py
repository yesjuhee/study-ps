n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
sum = 0
for i in range(n):
    sum += num_list[i] * (n - i)
print(sum)
