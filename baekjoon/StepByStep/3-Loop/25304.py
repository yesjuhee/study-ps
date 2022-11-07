# 영수증

sum = int(input())
num = int(input())
plist = []

for i in range(num):
    plist.append(list(map(int, input().split())))

cal = 0

for product in plist:
    cal += product[0]*product[1]

if cal == sum:
    print('Yes')
else:
    print('No')
