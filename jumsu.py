'''
점수 계산
'''

n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0
for x in a:   #리스트 원소에 차례대로 접근 하나하나씩
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)
        