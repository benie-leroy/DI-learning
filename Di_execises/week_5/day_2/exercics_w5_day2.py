class Animal():
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("{} barked, WAF !".format(self.name))