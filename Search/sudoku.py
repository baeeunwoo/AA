'''
2-10. 스도쿠 검사
'''


# ?? 왜 답이 NO로 나오나
# ch: 체크리스트 3개 필요 , 행 열 그룹 ch1 ch2 ch3
# ch1 [a[i][j]] = 1  : 0번행탐색 (가로)
# ch2 [a[j][j]] = 1 : 0열 체크(세로)
# sum(ch) != 9
# i*3+k 행  j*3+s 열
# ch3 = [0]*10 초기화

# 왜 0은 안쓴다 하신건지? ch 설명하실때 리스트가 1~9만 있었음

def check(b):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[b[i][j]] = 1
            ch2[b[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):  # 0 1 2
        for j in range(3):  # 0 1 2
            ch3 = [0] * 10  # 초기화
            for k in range(3):
                for s in range(3):
                    ch3[b[i * 3 + k][j * 3 + s]] = 1
                if sum(ch3) != 9:  # 9개인지 체크
                    return False  # 면 종료
        return True  # 중복이 없었다. (myThink:4중for문의 true라 젤 위 for 밑 한칸 들여쓰기?)


a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
