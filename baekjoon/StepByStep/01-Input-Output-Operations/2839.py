# 설탕 배달

N = int(input())
# N = a*5 + b*3

if 5 % N == 0:  # 5의 배수?
    print(int(N/5))
    exit()
else:
    a = int(N/5)
    if (N-a*5) % 3 == 0:  # 5의 배수를 빼고 남은 숫자가 3의 배수?
        b = int((N-a*5) / 3)
        print(a+b)
        exit()
    else:                 # a의 값을 줄여서 확인
        while (a > 0):
            a -= 1
            if (N-a*5) % 3 == 0:  # 5의 배수를 빼고 남은 숫자가 3의 배수?
                b = int((N-a*5) / 3)
                print(a+b)
                exit()

print(-1)
