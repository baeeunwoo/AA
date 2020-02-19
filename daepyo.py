'''
대표값
'''

import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n) #리스트에있는 모든 값 합해줌
min = 2147000000 #큰숫자
for idx, x in enumerate(a): #idx-x  인덱스-값 이렇게 보여줌
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x #답이되는점수도 저장
        res = idx + 1  #답이되는점수의학생번호
    elif tmp == min: #같은 거리를 갖는 학생의 성적이 나오면
        if x > score:
            score = x
            res = idx + 1
print(ave, res)