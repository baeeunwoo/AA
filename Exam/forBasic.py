'''
#빅뱅 멤버들
big_bang = ["지드래곤", "태양", "탑", "대성", "승리"]

i = 0

while i < len(big_bang):
    print(big_bang[i])
    i += 1


big_bang = ["지드래곤", "태양", "탑", "대성", "승리"]

for member in big_bang:
    print(member)


for num in [1, 3, 5, 7, 9]:  # for 변수 in 리스트/range/문자열:
    print(num * num)         #     <첫번째 실행>...


for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

# 1부터 100까지 수 출력
for i in range(1, 101):
    print(i)


for i in range(10):
    print(i)
'''

for i in range(6, 1, -1): # 이게 왜 6 5 4 3 2 인지 이해가 안감
    print(i)