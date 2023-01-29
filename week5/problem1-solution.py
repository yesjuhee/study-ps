# 떡볶이 떡 만들기 : 답안 예시

# 입력
n, m = map(int, input().split())
array = list(map(int, input().split()))

# 절단기 길이의 시작점과 끝점 설정
start = 0
end = max(array)

# 이진탐색 수행
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 모자란경우 -> 절단기의 크기 줄이기(왼쪽 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 같거나 많은 경우 -> 오른쪽 부분 탐색
    else:
        result = mid
        start = mid + 1

print(result)