#exercice 1: Cats
'''
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
cat1 = Cat('minou',2)
cat2 = Cat('jase',3)
cat3 = Cat('mindow',9)
def compare():
    if cat1.age > cat2.age and cat1.age > cat3.age:
        print('The oldest cat is {}, and is {} years old'.format(cat1.name, cat1.age))
    if cat2.age > cat1.age and cat2.age > cat3.age:
        print('The oldest cat is {}, and is {} years old'.format(cat2.name, cat2.age))
    if cat3.age > cat1.age and cat3.age > cat2.age:
        print('The oldest cat is {}, and is {} years old'.format(cat3.name, cat3.age))
compare()
'''

#exercice 1: autre methode
'''
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
cat1 = Cat('minou',2)
cat2 = Cat('jase',3)
cat3 = Cat('mindow',9)
def oldest(*args):
    old = args[0]
        for cat.age>old.age:
            if cat.age>old.age:
                old = cat
        :return max(args key=lambda cat : cat.age)

'''

#Exercise 2 : Dogs

'''
class Dog:
    def __init__(self, name, height):
        self.n = name
        self.h = height
    def bark(self):
        print('{} goes woof'.format(self.n))

    def jump(self):
        x = self.h*2
        print('{} jumps {} cm high'.format(self.n, x))

davids_dog = Dog('Rex', 50)
davids_dog.bark()
davids_dog.jump()
sarahs_dog = Dog('Teacup', 20)
sarahs_dog.bark()
sarahs_dog.jump()
def comparaison():
    if davids_dog.h > sarahs_dog.h:
        print('{} is the bigger dog'.format(davids_dog.n))
    if davids_dog.h < sarahs_dog.h:
        print('{} is the bigger dog'.format(sarahs_dog.n))
comparaison()
'''
#Exercise 3 : Who’s The Song Producer ?
'''
class Song:
    def __init__(self, lyrics):
        self.l = lyrics
    def sing_me_a_song(self):
       for i in self.l:
           print(i)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

'''

#Exercise 4 : Afternoon At The Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if self.animals.count(new_animal) == 0:
            self.animals.append(new_animal)
    def get_animals(self):
        for i in self.animals:
            print(i)
    def sell_animal(self, animal_sold):
        if self.animals.count(animal_sold) != 0:
            self.animals.remove(animal_sold)
    def sort_animals(self):


