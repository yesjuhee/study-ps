# 벌집

N = int(input())
shell = 1

# N==1인 경우
if N == 1:
    print(1)
    exit()

# N>1인 경우, shell을 하나씩 증가시켜 N이 해당 shell에 속하는지 확인
while (True):

    start = 3*shell**2 - 3*shell + 2
    end = 3*shell**2 + 3*shell + 1

    if start <= N and N <= end:
        print(shell+1)
        exit()

    shell += 1
