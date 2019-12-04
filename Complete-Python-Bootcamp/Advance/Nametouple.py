t = (1, 2, 3)
print(t[0])


from collections import namedtuple;
Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age = 2, breed='Lab', name='Sammy')
print(sam)
print('sam\'s age:{}'.format(sam.age))
print('sam\'s [0]:{}'.format(sam[0]))

Cat = namedtuple('Cat', 'fur claws name')
c = Cat(claws=False, name='Kitty', fur='Fuzzy')
print(c)
print('c\'s name:{}'.format(c.name))
print('c\'s [0]:{}'.format(c[1]))