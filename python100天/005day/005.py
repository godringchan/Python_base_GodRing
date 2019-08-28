# Craps赌博游戏
import random


while True:
    time = 1
    input("第{0}次投掷骰子".format(time))
    time += 1
    s1 = random.randint(1, 6)
    s2 = random.randint(1, 6)
    print("骰子one为{0}, 骰子two为{1}, 获得点数{2}".format(s1, s2, s1+s2))
    if s1 + s2 == 7 or s1 + s2 == 11:
        print("玩家胜利")
    elif (s1 + s2 == 2 or
        s1 + s2 == 3 or
        s1 + s2 == 12):
        print("点数为{0}庄家胜利，玩家失败".format(s1+s2))
    else:
        temp = s1 + s2
        while True:
            input("第{0}次投掷骰子".format(time))
            time += 1
            s1 = random.randint(1, 6)
            s2 = random.randint(1, 6)
            print("骰子one为{0}, 骰子two为{1}, 获得点数{2}".format(s1, s2, s1+s2))
            if s1 + s2 == 7:
                print("点数为7庄家胜利，玩家失败")
                break
            elif s1 + s2 == temp:
                # print("骰子one为{0}, 骰子two为{1}, 获得点数{2}".format(s1, s2, s1+s2))
                print("与首次相同，玩家胜利")
                break
    break
