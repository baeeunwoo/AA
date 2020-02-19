'''
2-1.k번째 약수
'''

# import sys
# sys.stdin = open("input.txt", "rt")
# n, k = map(int, input().split())  #띄어쓰기 구분 후 분리해서 읽음
# cnt = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         cnt += 1
#     if cnt == k:
#         print(i)
#         break
# else:               # 위 for문이 정상작동 했을 때 else로 넘어감
#     print(-1)

'''
2-2.k번째 작은수
'''
# import sys
# sys.stdin = open("input.txt", "rt")
#
# T = int(input())
# for t in range(T):
#     n, s, e, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     a = a [s - 1 : e]
#     print(a[1 : 5])   #1이 두번째 숫자 인덱스1이므로
#     a.sort()
#     print(a)
#     print("#%d %d" %(t + 1, a[k - 1]))

'''
k번째 큰 수 
'''

import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))