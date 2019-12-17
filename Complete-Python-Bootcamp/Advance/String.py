s = 'hello world'

# find & count
print ('find:' + str(s.find('o')))       # 找出o所在位置
print ('count:' + str(s.count('o')))     # 計算o出現次數

print('capitalize:' + s.capitalize())   # 首字母大寫 'Hello world'
print('upper:' + s.upper())             # 'HELLO WORLD'
print('lower:' + s.lower())             # 'hello world'


print('Lower Test'.istitle())

print('w'.endswith('w'))    # True
print('wow'.endswith('ow')) # True
print('wow'.endswith('wo')) # False

print('w'.startswith('w'))    # True
print('wow'.startswith('ow')) # False
print('wow'.startswith('wo')) # True