class SuperClass():
    def __init__(self, name):
        self.name = name

    def info(self):
        print(Hello, self.name)


class SubClass(SuperClass):
    def __init__(self, name):
        super().__init__(name)

    def info(self):
        print(Hi, self.name)

superc = SuperClass("An")
subc = SubClass("Bình")

print(superc.info())

print(subc.info())
