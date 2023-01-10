# 왕실의 나이트

# 입력
position = input()
#b2
row = int(position[1])
column = ord(position[0]) - 96

# 이동
# 8가지 이동의 경우의 수
drow =    [-2, -2, -1, -1, +2, +2, +1, +1]
dcolumn = [+1, -1, +2, -2, -1, +1, -2, +2]

# count
count = 0
for i in range(8):
    new_row = row + drow[i]
    new_column = column + dcolumn[i]
    if new_row in range(1, 9) and new_column in range(1, 9):
        count += 1

print(count)