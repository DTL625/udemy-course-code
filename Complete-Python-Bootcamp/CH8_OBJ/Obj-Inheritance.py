class Animal():
    def __init__(self):
        print('Animal Created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created!')

    def who_am_i(self):
        print('I am a dog')

    def bark(self):
        print('woof')


myanimal = Animal()
mydog.eat() # I am eating
myanimal.who_am_i() # I am an animal
mydog.bark() # error

mydog = Dog()
mydog.eat() # I am eating
myanimal.who_am_i() # I am a dog
mydog.bark() # woof
