# 곱셈

# 입력
import sys
num1 = int(sys.stdin.readline())
num2 = sys.stdin.readline()

# 계산
num3 = num1 * int(num2[2])
num4 = num1 * int(num2[1])
num5 = num1 * int(num2[0])
num6 = num3 + num4*10 + num5*100

# 출력
print(num3)
print(num4)
print(num5)
print(num6)
