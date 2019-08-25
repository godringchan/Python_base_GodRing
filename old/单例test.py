class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        # 1. 创建对象时，new 方法会被自动调用
        print('创建对象， 分配空间')
        # 2. 为对象分配空间
        if not cls.instance:
            # 当 instance 为None 执行，super要指定继承自己，传递cls类对象
            cls.instance = super().__new__(cls, *args, **kwargs)

        # 3. instance已经存在就返回对象的引用
        return cls.instance

    def __init__(self):
        print('播放器初始化')

# class Base(MusicPlayer):
    a = 1


player1 = MusicPlayer()
player2 = MusicPlayer()

print(player1)
print(player2)
