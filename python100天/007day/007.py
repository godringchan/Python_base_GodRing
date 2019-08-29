# 双色球
import random


def select_balls():
    """
    抽取双色球
    """
    balls = [x for x in range(1, 34)]
    balls = random.sample(balls, 6)
    balls.sort()
    balls.append(random.randint(1, 16))
    return balls


# def show_balls(balls):
#     for index, ball_num in enumerate(balls):
#         if index == len(balls) - 1:
#             print("|", end="")
#         print("%02d" % ball_num, end=" ")
def show_balls(balls):
    """
    显示抽取到的双色球号码
    """
    flag = 0
    for i in balls:
        if flag == len(balls) - 1:
            print("|", end="")
        print("%02d" % i, end=" ")
        flag += 1


def main():
    times = int(input("买几注双色球"))
    for _ in range(times):
        show_balls(select_balls())
        print()


if __name__ == "__main__":
    main()
