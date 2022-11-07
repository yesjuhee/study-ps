# 분수 찾기

order = int(input())
n = 0

while True:
    if order <= (n+1)*(n+2)/2:
        n += 1
        break
    n += 1
print(f'n:{n}')

dis = order - n*(n-1)/2 - 1  # 시작 번호에서 몇 칸 떨어졌냐?
print(f'dis:{dis}')

if n % 2 == 0:  # 짝수라면
    start = [1, n]
    start[0] += dis
    start[1] -= dis
else:
    start = [n, 1]
    start[0] -= dis
    start[1] += dis

print(f'{int(start[0])}/{int(start[1])}')
