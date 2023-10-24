# 과제 안 내신 분..?

# 1~30까지 모두 가지고 있는 리스트
numberList = list(range(1, 31))

# 28번 입력 받으면서 삭제
for _ in range(28):
    deleteNumber = int(input())
    numberList.remove(deleteNumber)

# 출력
print(numberList[0])
print(numberList[1])
