# 나머지

nlist = []
for i in range(10):
    nlist.append(int(input()) % 42)

print(len(set(nlist)))
