# 상수


a, b = input().split()

a_rev = a[::-1]
b_rev = b[::-1]


if int(a_rev) > int(b_rev):
    print(a_rev)
else:
    print(b_rev)
