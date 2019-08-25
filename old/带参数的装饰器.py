def add_test(a):
    def call_app(func):
        if a == 1:
            def call_test(*args, **kwargs):
                print("add_1")
                return func(*args, **kwargs)
            return call_test
        if a == 2:
            def call_test2(*args, **kwargs):
                print("add_2")
                return func(*args, **kwargs)
            return call_test2
    return call_app


@add_test(1)
def test():
    print("test")


test()