array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        # 종료 조건
        # start == end -> 파티션에 존재하는 원소의 개수가 1개임을 의미
        # start > end  -> 파티션에 원소가 존재하지 않음을 의미
        return

    pivot = start       # 피벗을 기준으로 작은 원소는 왼쪽으로, 큰 원소는 오른쪽으로 분할
    left = start + 1    # 왼쪽에서 피벗보다 큰 원소를 찾아서 오른쪽으로 보낸다
    right = end         # 오른쪽에서 피벗보다 작은 원소를 찾아서 왼쪽으로 보낸다

    while (left <= right):  # left와 right가 교차되면 반복문 종료
        while (left <= end and array[left] <= array[pivot]):
            # left는 왼쪽부터 피벗보다 큰 원소를 찾을 때까지 오른쪽으로 한 칸씩 이동한다.
            left += 1
        while (right > start and array[right] >= array[pivot]):
            # right는 오른쪽부터 피벗보다 작은 원소를 찾을 때까지 왼쪽으로 한 칸씩 이동한다.
            right -= 1

        if (left > right):
            # left와 right가 교차되면 피벗위치의 원소와 right위치의 원소를 swap한다
            # 즉, 분할을 시행하고 반복문이 종료된다
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # left와 right가 교차되지 않았다면 두 원소를 swap한 후 반복한다
            array[left], array[right] = array[right], array[left]

    # right의 위치로 피벗 원소가 이동하고 분할이 완료되었기 때문에
    # 나뉜 두 부분에 대해 다시 sort를 진행한다.
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
