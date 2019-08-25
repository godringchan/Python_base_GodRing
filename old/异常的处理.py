class BigError(BaseException):
    pass


def big():
    b = input("int")
    b = int(b)
    try:
        if b > 100:
            raise BigError
        else:
            print("right")
    except BigError:
        print("cuowu")

if __name__ == "__main__":
    big()