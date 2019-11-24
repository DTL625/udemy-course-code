import sys

def create_init_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

for x in create_init_cubes(10):
    # print(x, end=' ')
    pass
# print("\n")
# --------------------------------

def create_cubes(n):
    for i in range(n):
        yield i**3

r = create_cubes(10)
# print(r)
# print(list(r))

# --------------------------------
# print(create_cubes(10).__sizeof__())
# print(create_init_cubes(10).__sizeof__())

# --------------------------------
def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for num in gen_fibon(10):
    # print(num)
    pass

# --------------------------------
def simple_gen():
    mylist = range(5)
    for x in mylist:
        yield x

for number in simple_gen():
    print(number, end = ' ')
#
print('\n--------------')
#
g = simple_gen()
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
print(next(g))  # 4
print(next(g))  # get error