array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 종료 조건 : 분할된 리스트가 하나 이하의 원소만을 담고 있는 경우
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]  # 왼쪽 분할 : 피벗보다 크기가 작은 원소들
    right_side = [x for x in tail if x > pivot]  # 오른쪽 분할 : 피벗보다 크기가 큰 원소들

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
