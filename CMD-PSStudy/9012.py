# 괄호

import sys
input = sys.stdin.readline


def input_pop(stack):
    return stack.pop(), stack


def compare_p(x, stack):
    if len(stack) == 0:
        stack.append(x)
        stack
    if x == stack[-1]:
        stack.pop()
        return stack
    stack.append(x)
    return stack


n = int(input())
check_stack = []

for _ in range(n):
    input_stack = list(input())
    input_stack = input_stack[0:-1]
    for _ in range(len(input_stack)):
        x_input_pop, input_stack = input_pop(input_stack)
        check_stack = compare_p(x_input_pop, check_stack)
    if len(check_stack) == 0:
        print("YES")
    else:
        print("NO")
