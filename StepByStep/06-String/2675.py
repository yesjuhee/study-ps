# 문자열 반복

n = int(input())

for _ in range(n):
    num, word = input().split()
    num = int(num)
    new_word = ''
    for letter in word:
        new_word += letter * num
    print(new_word)
