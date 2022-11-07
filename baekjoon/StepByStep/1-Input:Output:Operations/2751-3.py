# 수 정렬하기 2

# 입력
import sys
sys.setrecursionlimit(10**6)
n = int(input())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

# 정렬 (퀵 정렬)


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = len(array) // 2
    front_arr, pivot_arr, back_arr = [], [], []
    for value in array:
        if value < array[pivot]:
            front_arr.append(value)
        elif value > array[pivot]:
            back_arr.append(value)
        else:
            pivot_arr.append(value)
    return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)


arr = quick_sort(arr)

# 출력
for i in arr:
    print(i)
