# 소트 인사이트

number = input()
number_partition = list(map(int, list((number))))
number_partition.sort(reverse=True)
print(''.join(map(str, number_partition)))
