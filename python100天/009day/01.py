from time import localtime, sleep


class Clock(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def now(cls):
        time_now = localtime()
        return cls(time_now.tm_hour, time_now.tm_min, time_now.tm_sec)

    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):

        '''
        显示时间
        '''
        return "现在时间是%02d时%02d分%02d秒" % (self.hour, self.minute, self.second)


def main():
    c_clock = Clock.now()
    while True:
        c_clock.run()
        sleep(1)
        print(c_clock.show(), end="\r")


if __name__ == "__main__":
    main()
