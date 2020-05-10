
from random import randint

# 상수
ANSWER = randint(1, 20)

# 변수
tries = 1
chance = 4


# 시도 남은 경우

while tries <= 4:

    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % chance))

    if guess < ANSWER:
        print("Up")
    elif guess > ANSWER:
        print("Down")
    elif guess == ANSWER:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % tries)
        break

    chance = chance - 1
    tries = tries + 1

# 시도 남지 않은 경우

if chance == 0:
    print("아쉽습니다. 정답은 %d였습니다." % ANSWER)