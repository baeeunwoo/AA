'''
자리수
'''

import sys
# sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
# 이 부분 위 코드로 대체 가능
#     while x > 0:
#         sum += x % 10
#         x = x // 10

    return sum
max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)
