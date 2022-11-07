# 단어의 개수

sentence = input()

if len(sentence) == 0 or len(sentence) == sentence.count(' '):
    print(0)
else:
    while sentence[0] == ' ' or sentence[-1] == ' ':
        if sentence[0] == ' ':
            sentence = sentence[1:]
        elif sentence[-1] == ' ':
            sentence = sentence[:-1]
    print(1+sentence.count(' '))
