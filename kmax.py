'''
k번째 큰 수
'''

# import sys
# sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()  #중복제거
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(a[i] + a[j] + a[m])
res = list(res) #set는 sort가안됨
res.sort(reverse = True)
print(res[k - 1])