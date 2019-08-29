# 练习1：在屏幕上显示跑马灯文字
# import os
import time


def main():
    connect = "天王盖地虎，宝塔镇河妖   "

    while True:
        # os.system("cls")  # 清理屏幕
        print(connect, end="\r")  # 不清理屏幕覆盖在同一行
        time.sleep(0.2)  # 暂停0.2秒
        connect = connect[1:] + connect[0]


if __name__ == "__main__":
    main()
