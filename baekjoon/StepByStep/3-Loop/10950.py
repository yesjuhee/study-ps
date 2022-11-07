# A+B - 3

n = int(input())
nlist = []

for i in range(n):
    nlist.append(list(map(int, input().split())))

for nums in nlist:
    print(nums[0]+nums[1])
