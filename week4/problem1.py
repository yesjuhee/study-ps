# 두 배열의 원소 교체

# 입력
n, k = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

# 정렬
array_a.sort()
array_b.sort(reverse=True)

# 바꿔치기
for i in range(k):
    if array_a[i] < array_b[i]:
        array_a[i] = array_b[i]
    else:
        break
# 출력
print(sum(array_a))
