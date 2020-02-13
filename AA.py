'''
2-1.k번째 약수
'''

import sys
# sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())  #띄어쓰기 구분 후 분리해서 읽음
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:               # 위 for문이 정상작동 했을 때 else로 넘어감
    print(-1)