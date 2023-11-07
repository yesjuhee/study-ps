# 문자열 뒤집기

import sys
import re
input = sys.stdin.readline

s = input()

if (int(s[0])):
    print(len(re.findall("10", s)))
else:
    print(len(re.findall("01", s)))
