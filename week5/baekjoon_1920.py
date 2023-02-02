# 수 찾기

import sys
input = sys.stdin.readline

# 입력
n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int, input().split()))

# 이진 탐색
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# M개의 수에 대한 이진탐색 결과 출력
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for x in arr2:
    if binary_search(arr1, x, 0, n-1) == None:
        print(0)
    else:
        print(1)
