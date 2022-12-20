# 소인수분해

# for문을 사용하면 너무 오래걸림
# while문을 사용해서 더이상 나눠야할 필요가 없으면 반복문이 중단되도록 설정

n = int(input())
divisor = 2

while n != 1:
    if n % divisor == 0:
        print(divisor)
        n = n//divisor
    else:
        divisor += 1
