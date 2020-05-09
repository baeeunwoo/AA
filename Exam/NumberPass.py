from random import randint

# 상수
ANSWER = randint(1, 20)

# 변수
chance = 4
tries = 1

# 기회 남았을 떄
while tries <= 4:

    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % chance))

    if ANSWER > guess:
        print("UP")
    elif ANSWER < guess:
        print("Down")
    elif ANSWER == guess:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (tries))
        break
    chance = chance - 1
    tries = tries + 1

# 기회 없을 떄
if chance == 0:

    print("아쉽습니다. 정답은 %d였습니다." % (ANSWER))
