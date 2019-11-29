class Student(object):
    def __init__(self, n={"name": "",
                          "score": "",
                          "sex": ""}):
        self.name = n["name"]
        self.score = n["score"]
        self.sex = n["sex"]

    def say_score(self):
        print(self.score)

    def say_name(self):
        print(self.name)

    def say_sex(self):
        print(self.sex)

    def __call__():

    

    @staticmethod
    def print_say():
        print("哈哈哈")


if __name__ == "__main__":

    n = {"name": "ring",
         "score": 100,
         "sex": "male"}
    s1 = Student(n)
    s1.say_score()
    s1.say_name()
    s1.say_sex()
    s1.print_say()
    print(s1.__dict__) 