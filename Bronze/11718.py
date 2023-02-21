# 그대로 출력하기

while True:
    try:
        line = input()
        print(line)
    except EOFError:
        break

