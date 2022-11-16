# 소인수분해

import sys
input = sys.stdin.readline

# 10,000,000 이하의 소수 리스트 만들기
max_number = 10000000
is_primenumber = [True]*(max_number+1)
is_primenumber[0] = False
is_primenumber[1] = False

for x in range(2, int(max_number**0.1)+1):
    if is_primenumber[x] == True:
        step = 2
        while x*step <= max_number:
            is_primenumber[x*step] = False
            step += 1

primenumber_list = [x for x in range(
    2, max_number+1) if is_primenumber[x] == True]


# 입력 받기
number = int(input())

# 소수 리스트에서 하나씩 꺼내면서 인수에 해당하면 출력
for primenumber in primenumber_list:
    while number % primenumber == 0:
        print(primenumber)
        number = number // primenumber
