class MusicPlayer():
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            # return cls.instance
        return cls.instance


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
