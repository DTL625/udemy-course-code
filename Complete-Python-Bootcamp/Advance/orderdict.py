from collections import OrderedDict
# ----- Normal dictionary-----
normal_dict = {}

normal_dict['1'] = "one"
normal_dict['2'] = "two"
normal_dict['3'] = "three"
normal_dict['4'] = "four"
normal_dict['5'] = "five"
print('origin:', end=' ')
for k, v in normal_dict.items():
    print(f'[{k}]{v}', end=' ')

od = OrderedDict()

od['a'] = 1
od['d'] = 5
od['e'] = 4
od['c'] = 2
od['b'] = 3
print('order dict', end=' ')
for k, v in od.items():
    print(f'[{k}]{v}', end=' ')

print("\n")
# ----
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'
print(f'Dictionaries are equal? ', end=' ')
print(d1==d2)

# ----
d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'

d2 = OrderedDict()

d2['b'] = 'B'
d2['a'] = 'A'
print(f'Dictionaries are equal? ', end=' ')
print(d1==d2)