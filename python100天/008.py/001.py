# 定义一个时钟类
import time


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.running = "on"
        self.minute = minute
        self.hour = hour
        self.second = second
        self.mini_second = 0

    def run(self):
        self.mini_second += 1
        if self.mini_second == 10:
            self.second += 1
            self.mini_second = 0
            if self.second == 60:
                self.minute += 1
                self.second = 0
                if self.minute == 60:
                    self.hour += 1
                    self.minute = 0
                    if self.hour == 24:
                        self.hour = 0

    def show_the_time(self):
        return "现在时间是%02d时%02d分%02d秒%02d" % \
            (self.hour, self.minute, self.second, self.mini_second)

    def turn_run(self):
        '''
        时钟的开关
        '''
        if self.running == "on":
            self.running = "off"
            print("关闭时钟")
        else:
            self.running = "on"

    def rec_clock(self, hour=0, minute=0, second=0):
        '''
        重置时钟为
        '''
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def stop_run():
        '''
        暂停时钟
        '''
        stop = input("时间暂停按任意键继续")
        return stop


def main():
    times = 100
    clock_one = Clock()
    while clock_one.running == "on":
        clock_one.run()
        time.sleep(0.1)
        print(clock_one.show_the_time(), end="\r")
        times -= 1
        if times == 60:               # 达到条件停止时钟
            print()
            clock_one.stop_run()

        if times == 50:               # 达到条件关闭时钟
            print()
            clock_one.turn_run()


if __name__ == "__main__":
    main()
