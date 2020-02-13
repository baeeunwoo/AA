'''
k번째 약수 연습
'''

import sys
sys.stdin = open("input2.txt", "rt")

n, k = map(input().split())
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i) # 여기를 잘 모르겠 다시 들어보기
        break

else:
    print(-1)