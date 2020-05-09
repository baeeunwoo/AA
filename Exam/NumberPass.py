from random import randint

ANSWER = randint(1, 20)

chance = 4
tries = 0

while tries < 4:

    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % chance))

    if ANSWER > guess:
        print("UP")
    elif ANSWER < guess:
        print("Down")
    else:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (5 - tries))
        break
    chance = chance - 1
    tries = tries + 1

if tries == 0:

    print("아쉽습니다. 정답은 %d였습니다." % (ANSWER))
