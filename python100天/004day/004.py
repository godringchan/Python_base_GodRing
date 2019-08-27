# 猜数字游戏
import random
answer = random.randint(1, 100)
flag = 0
while True:
    flag += 1
    guess = int(input("猜一猜，数字是多少"))
    if guess > answer:
        print("大了一点")
    elif guess < answer:
        print("小了一点")
    elif guess == answer:
        print("恭喜你猜对了")
        break
if flag > 7:
    print("你的智商欠费")