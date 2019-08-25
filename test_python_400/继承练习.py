class Person(object):

    def __init__(self, *args, **kwargs):
        pass

    def mai(self):
        pass


class Student(Person):

    def __init__(self, *args, **kwargs):
        pass
        #  super().__init__(*args, **kwargs)

    def mai(self):
        super().mai()


