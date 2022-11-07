# 알람 시계

# 입력
import sys
H, M = map(int, sys.stdin.readline().split())

# 시간을 모두 분으로 변환
time = H*60 + M
time -= 45

# 다시 시간으로 변환
if time >= 0:
    H = time // 60
    M = time % 60
else:
    H = 23
    M = 60+time

print(f'{H} {M}')
