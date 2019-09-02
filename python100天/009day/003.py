from abc import ABCMeta, abstractmethod
# import random
from random import randint, randrange


class Figther(object, metaclass=ABCMeta):
    __slots__ = ("_name", "_hp")

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if self._hp > 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class Ultraman(Figther):
    _slots_ = ("_name", "_hp", "_mp")

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp
    
    def attack(self, other):
        other._hp -= randint(10, 20)
    
    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp*3//4
            injury = injury if injury > 50 else 50
            self.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(15, 20)
            return True
        else:
            return False

    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return self._mp

    def __str__(self):
        return "~~~%s奥特曼生命值~~~\n" % self._name + \
            "生命：%d \n" % self._hp + \
            "魔法：%d \n" % self._mp


class Monster(Figther):

    __slot__ = ("_name", "_hp")

    def attack(self, other):
        other.hp -= randint(10, 15)

    def __str__(self):
        return "~~~%s小怪兽~~~~\n" % self._name +\
                "生命:%d~~\n" % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive:
            return True
        else:
            return False


def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index] 
        if monster.alive:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end="")


def main():
    u = Ultraman("咸蛋", 1000, 1000)
    m1 = Monster("哥斯拉", 250)
    m2 = Monster("哥拉斯", 200)
    m3 = Monster("拉哥斯", 300)
    ms = [m1, m2, m3]
    figther_round = 1
    while u.alive and is_any_alive(ms):
        print("*******第%02d回合攻击******" % figther_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill <= 6:
            print("%s奥特曼攻击%s怪兽" % (u, m))
            u.attack(m)
            print("%s奥特曼回复%d点mp" % (u, u.resume()))
        elif skill <= 9:
            print("%s奥特曼发起魔法攻击" % u)
            if u.magic_attack(ms):
                print("攻击成功")
            else:
                print("法力不足")
                print("%s奥特曼攻击%s怪兽" % (u, m))
                u.attack(m)
                print("%s奥特曼回复%d点mp" % (u, u.resume()))
        else:
            if u.huge_attack(m):
                print("%s奥特曼释放必杀技攻击%s" % (u, m))
            else:
                print("发力不足")
                print("%s奥特曼攻击%s怪兽" % (u, m))
                u.attack(m)
                print("%s奥特曼回复%d点mp" % (u, u.resume()))
        if m.alive:
            print("%s反击了" % m)
            m.attack(u)
        display_info(u, ms)
        print("""
              *
              *
              *
              """)
        figther_round += 1
    print("战斗结束")
    if u.alive:
        print("%s奥特曼胜利" % u)
    else:
        print("怪兽胜利了")


if __name__ == "__main__":
    main()
