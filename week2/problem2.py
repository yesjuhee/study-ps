# 곱하기 혹은 더하기

# 입력
string = input()

max = int(string[0])

for i in range(1, len(string)):
    num = int(string[i])
    # 둘 중 하나가 0인 경우 더하기
    if max * num == 0:
        max += num
    # 둘 중 하나가 1인 경우 더하기
    elif max == 1 or num == 1:
        max += num
    # 이외의 모든 경우는 빼기
    else:
        max *= num

print(max)
