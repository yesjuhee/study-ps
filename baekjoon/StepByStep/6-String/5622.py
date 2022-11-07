# 다이얼

info_list = [['ABC', 3], ['DEF', 4], ['GHI', 5], ['JKL', 6],
             ['MNO', 7], ['PQRS', 8], ['TUV', 9], ['WXYZ', 10]]
word = input()
time = 0

for letter in word:
    for info in info_list:
        if letter in info[0]:
            time += info[1]

print(time)
