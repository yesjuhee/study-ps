array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):  # i : 앞 부분에 삽입할 원소의 인덱스
    for j in range(i, 0, -1):   # j를 이용해서 삽입할 원소의 위치를 앞으로 한칸 씩 이동시킨다.
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            # 이미 i의 앞 쪽은 오름차순 정렬이 되어있으므로
            # 자기보다 작은 숫자가 앞에 위치할 때까지 이동한 다음에 이동을 종료한다.
            break

print(array)
