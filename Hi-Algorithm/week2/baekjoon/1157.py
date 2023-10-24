# 단어 공부

str = input()
str = str.upper()
letter_count = -1

for letter in set(str):
    if letter_count == str.count(letter):
        output = '?'
    elif letter_count < str.count(letter):
        output = letter
        letter_count = str.count(letter)

print(output)
