d = {'k1':1,'k2':2}

print('init dict: {}'.format(d))
print('- dict.keys: {}'.format(d.keys()))
print('- dict.values: {}'.format(d.values()))
print('\n')
d['k3'] = 3
print('new dict: {}'.format(d))
print('- dict.keys: {}'.format(d.keys()))
print('- dict.values: {}'.format(d.values()))
print('\n')

y = {x:x**2 for x in range(5)}
print(y) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

y = {k:v**2 for k, v in zip(['a', 'b'], range(2))}
print(y) # {'a': 0, 'b': 1}
