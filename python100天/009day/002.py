from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    def __init__(self, nick_name):
        self._nick_name = nick_name

    @abstractmethod
    def make_vioce(self):
        '''
        发出声音
        '''
        pass


class Dog(Pet):
    '''
    重写
    '''
    def make_vioce(self):
        print("%s..汪汪汪" % self._nick_name)


class Cat(Pet):
    def make_vioce(self):
        print("%s...喵喵喵" % self._nick_name)


def main():
    pets = [Dog("旺财"), Cat("凯莉"), Dog("秋田")]
    for pet in pets:
        pet.make_vioce()


if __name__ == "__main__":
    main()