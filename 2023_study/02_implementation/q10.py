# 자물쇠와 열쇠

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# lock = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1]]

n = len(key)
m = len(lock)
k = n + m - 1

# 회전 (4번 반복)
for _ in range(4):
    temp_key = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp_key[j][(n - 1) - i] = key[i][j]
    key = temp_key

    # k^2번 key를 이동 -> 비교
    for i in range(k):
        for j in range(k):
            # (i, j) 위치에 k_key 만들기 (이동)
            k_key = [[-1] * k for _ in range(k)]
            for x in range(n):
                for y in range(n):
                    # 인덱스 범위 확인
                    if (i + x) < k and (j + y) < k:
                        k_key[i + x][j + y] = key[x][y]

            result = True
            # k_key와 lock 비교
            for x in range(m):
                for y in range(m):
                    if lock[x][y] == 0:
                        if k_key[x + (k - m)][y + (k - m)] != 1:
                            result = False
                    elif lock[x][y] == 1:
                        if k_key[x + (k - m)][y + (k - m)] == 1:
                            result = False

            if (result):
                # return result
                print("success")
