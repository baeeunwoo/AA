'''
2-2. 숫자만 추출
'''

s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)
cnt = 0
for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1
print(cnt)