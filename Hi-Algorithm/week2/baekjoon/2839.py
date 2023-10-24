# 설탕 배달

n = int(input())

# n = 5 * a + 3 * b
a = n // 5

while a >= 0:
    gap = n - a * 5
    if gap % 3 == 0:
        print(a + gap//3)
        exit()
    else:
        a -= 1

print(-1)