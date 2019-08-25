class OnlyOne():
    a = None

    def __new__(cls):
        if not cls.a:
            cls.a = super(OnlyOne, cls).__new__(cls)
        return cls.a


class Player(OnlyOne):
    pass


Player1 = Player()
Player2 = Player()

print(Player1)
print(Player2)
