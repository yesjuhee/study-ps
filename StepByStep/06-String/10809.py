# 알파벳 찾기

word = input()

alpha_list = [-1]*26

for letter in word:
    # 단어 하나씩 체크해서 존재하면 list바꾸기
    # a : 97 / z : 122
    asci = ord(letter)-97
    alpha_list[asci] = word.index(letter)

print(' '.join(map(str, alpha_list)))
