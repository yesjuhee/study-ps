# 문자열 재정렬

# 입력
input_data = list(input())
sum = 0
string_list = []

for data in input_data:
    if data.isdigit():
        sum += int(data)
    else:
        string_list.append(data)

string_list.sort()
print(''.join(string_list)+str(sum))
