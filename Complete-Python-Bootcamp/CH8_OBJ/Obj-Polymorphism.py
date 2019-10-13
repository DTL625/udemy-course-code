class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' say woof!'


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' say meow!'




niko = Dog('niko')
felix = Cat('felix')


def pet_speak(pet):
    print(pet.speak())

for pet in [niko, felix]:
    print(type(pet))
    # print(pet.speak( ))
    pet_speak(pet)


