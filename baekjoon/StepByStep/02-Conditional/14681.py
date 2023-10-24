# 사분면 고르기

# 입력
x = int(input())
y = int(input())

# 출력
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
