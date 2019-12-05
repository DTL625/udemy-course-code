from collections import OrderedDict
# ----- Normal dictionary-----
normal_dict = {}

normal_dict['a'] = "one"
normal_dict['b'] = "two"
normal_dict['c'] = "three"
normal_dict['d'] = "four"
normal_dict['e'] = "five"

print(normal_dict)
# ----- Order dictionary v1-----
order_dict = OrderedDict(normal_dict)
print(order_dict)
# ----- Order dictionary v2-----
order_dict2 = OrderedDict()
order_dict2['c'] = "three"
order_dict2['a'] = "one"
order_dict2['b'] = "two"
order_dict2['e'] = "five"
order_dict2['d'] = "four"
print(order_dict2)





# print("\n")
# ----
# d1 = {}
# d1['a'] = 'A'
# d1['b'] = 'B'
#
# d2 = {}
# d2['b'] = 'B'
# d2['a'] = 'A'
# print(f'Dictionaries are equal? ', end=' ')
# print(d1==d2)
#
# # ----
# d1 = OrderedDict()
# d1['a'] = 'A'
# d1['b'] = 'B'
#
# d2 = OrderedDict()
#
# d2['b'] = 'B'
# d2['a'] = 'A'
# print(f'Dictionaries are equal? ', end=' ')
# print(d1==d2)