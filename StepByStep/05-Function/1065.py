# 한 수

n = int(input())

for num in range(1, n+1):
    num_arr = list(map(int, str(num)))
    # 1자리, 2자리 수는 패스
    if len(num_arr) == 1 or len(num_arr) == 2:
        continue

    # 3자리 수 이상일 때 한 수인지 체크
    diff = num_arr[0] - num_arr[1]
    for index in range(1, len(num_arr)-1):
        if diff != (num_arr[index]-num_arr[index+1]):
            n -= 1
            break

print(n)
