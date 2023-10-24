# 이진 탐색 - 재귀 함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# n : 원소의 개수
# target : 찾고자 하는 값
n, target = list(map(int, input().split()))

# 전체 원소 입력
array = list(map(int, input().split()))

# 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)