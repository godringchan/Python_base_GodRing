# 练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
from math import sqrt


class Point(object):
    def __init__(self, x=0, y=0):
        # super().__init__(*args, **kwargs)
        self.x = x
        self.y = y
    
    def move_to(self, x, y):
        self.x = x
        self.y = y
    
    def move_left(self, x):
        self.x -= x
    
    def move_right(self, x):
        self.x += x
    
    def move_up(self, y):
        self.y += y
        
    def move_down(self, y):
        self.y -= y
    
    def __str__(self):
        return "位置于x：%02d,y:%02d" % (self.x, self.y)

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)


def main():
    p1 = Point(1, 23)
    p2 = Point(2, 13)
    p1.move_down(100)
    print(p1)
    p2.move_right(50)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == "__main__":
    main()
