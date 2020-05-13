
'''
#value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        #some_list에서 value를 찾으면 True 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했다면 False 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))



primes = [2, 3, 5, 7, 11, 17, 19, 23]
print(7 in primes)
print(27 in primes)

#없는지 확인
print(7 not in primes)
print(27 not in primes)


#세 번의 시험을 봄
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

#첫 번째 학생 성적
print(grades[0])

#세 번쨰 학생 성적
print(grades[2])

#첫 번쨰 시험 평균
print(int(s[2][0]) / 3))(grades[0][0] + grades[1][0] + grade

# sort 메소드

numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)

numbers = sorted(numbers)
print(numbers)


# reverse - 뒤집어진 순서로 배치
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)
'''

# index - 원소의 인덱스 리턴
members = ["옥옥", "딸랑", "선윤", "하라"]
print(members.index("딸랑"))

# remove - 첫 번쨰로 x의 값을 갖고 있는 원소 삭제
fruits = [ "딸기", "당근", "파인애플", "수박", "참외", "메론", "자몽", "딸기", "파인애플"]
fruits.remove("딸기")
print(fruits)