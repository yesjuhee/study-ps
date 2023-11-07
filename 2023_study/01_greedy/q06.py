# 무지의 먹방 라이브

# 시간 초과 발생

def solution(food_times, k):

    # 가능 불가능 판단
    if (sum(food_times) <= k):
        return -1

    food_index = 0
    for i in range(k):
        # food_index 음식을 다 먹었으면 넘긴다
        while (food_times[food_index] == 0):
            food_index = (food_index + 1) % len(food_times)
        food_times[food_index] -= 1
        food_index = (food_index + 1) % len(food_times)

    while (food_times[food_index] == 0):
        food_index = (food_index + 1) % len(food_times)

    return food_index + 1
