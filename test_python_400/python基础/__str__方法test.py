class person:
    def __init__(self, name):
        self.name = name
        self.dict = {"a": 123,
                     "b": 234,
                     }

    def __str__(self):
        return "名字叫{0}".format(self.name) + "名字叫%s" % self.name


if __name__ == "__main__":
    p = person("jack")
    print(p)
