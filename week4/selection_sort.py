array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):  # i는 0부터 마지막 인덱스까지, 정렬이 될 원소를 가리킴
    min_index = i
    for j in range(i + 1, len(array)):  # 0 ~ i-1 까지는 정렬이 됐으므로 그 뒷 부분을 확인
        if array[min_index] > array[j]:  # j 인덱스로 끝까지 돌면서 최소값을 선택
            min_index = j
    # i의 위치에 선택한 최소값으로 swap
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
