# 그룹 단어 체커
# 단어 N개를 입력 받아 그룹 단어의 개수 출력

# 입력
import sys
n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(sys.stdin.readline())

# 중복된 문자 제거
for i in range(len(arr)):
    prev = None
    chars = []
    for char in arr[i]:
        if prev != char:
            chars.append(char)
            prev = char
    arr[i] = chars


# 그룹 단어 카운트
# 그룹 단어 ->  단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우
# 그룹 단어가 아닌 것 -> 단어에 존재하는 어떤 문자 하나라도, 각 문자가 연속해서 나타나지 않는 경우
# 그룹 단어가 아닌 것 카운트
# 단어 하나를 잡고 끝까지 반복문을 돌렸을 때 같은 것이 있다면 그룹 단어가 아님
count = 0
for word in arr:  # n개의 단어를 하나씩 확인
    if len(word) == len(set(word)):
        count += 1

print(count)
