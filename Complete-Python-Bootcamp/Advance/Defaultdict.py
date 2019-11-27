from collections import defaultdict

d = {'k1':1}

print(f"print k1: {d['k1']}") # 1
print(f"print k2: {d['k2']}") # get error

dd = defaultdict(object);
print(f"print k3: {dd['k3']}") # <object object at 0x10e485180>
print(f"print k4: {dd['k4']}") # <object object at 0x10e485190>

dd['k5'] = 'foooooo';
print(f"print k5: {dd['k5']}") # foooooo
print(dd)


dd = defaultdict(lambda : 0);
print(f"print k6: {dd['one']}") #
dd['two'] = '1';
print(dd)