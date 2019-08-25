# 单例额练习，单例要处理new方法，和init方法
# new方法，处理内存唯一
# init方法处理初始化为一


class MusicPlayer:
    __obj = None
    __init_flag = True

    def __new__(cls):
        if MusicPlayer.__obj is None:
            MusicPlayer.__obj = super().__new__(cls)
        return MusicPlayer.__obj

    def __init__(self):
        if MusicPlayer.__init_flag:
            print("MusicPlayer启动")
            MusicPlayer.__init_flag = False


m = MusicPlayer()
print(m)
m1 = MusicPlayer()
print(m1)
