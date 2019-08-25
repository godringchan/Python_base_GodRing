def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("___level_1____")
            if level_num == 2:
                print("__level_2___")
            return func(*args, **kwargs)
        return call_func
    return set_func


@set_level(2)
def test():
    print("test")


if __name__ == "__main__":
    test()
