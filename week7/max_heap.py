# 힙 라이브러리 사용 예제 : 최대 힙
import heapq

# 내림차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # pop
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
