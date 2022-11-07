# 셀프 넘버

# d(n)
def d(n):
    sum1 = [int(i) for i in str(n)]
    ssum = sum(sum1)
    return n + ssum


# 1~10000 리스트
nlist = list(range(1, 10001))
dlist = []

# 하나씩 구하기
for x in nlist:
    dlist.append(d(x))

# 차 집합
plist = list(set(nlist).difference(dlist))
plist.sort()
# 출력
for x in plist:
    print(x)
