'''
2-9. 봉우리
'''


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]    #12시,3시,6시,9시 방향으로 이동하며 탐색
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0] * n)  #0으로된행렬 0행에 추가
a.append([0] * n)  #마지막행에 0으로된행렬 추가
for x in a:
    x.insert(0, 0)  # 양끝에 0추가???
    x.append(0)

cnt = 0
for i in range(1, n + 1):  #1열?부터 돌아야하니, 양끝은0이니
    for j in range(1, n + 1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)): #상하좌우 탐색
            cnt += 1
print(cnt)