s = set()

# add
s.add(1)
s.add(2)
print('set add:{}'.format(s)) # {1, 2}

# clear
s.clear()
print('set clear:{}'.format(s)) # set()

# copy
s = {1, 2, 3}
sc = s.copy()
print('set copy:')
print(' - set s:{}'.format(s)) # {1, 2, 3}
print(' - set sc:{}'.format(sc)) # {1, 2, 3}

# diff 返回一个移除相同元素的新集合
s.add(4)
print('set difference:')
print('- s.difference(sc) : {}'.format(s.difference(sc))) # 4，元素包含在集合 s ，但不在集合 sc
print('- sc.difference(s) :{}'.format(sc.difference(s))) # set()，元素包含在集合 sc ，但不在集合 s


# difference_update 在原集合中，移除两个集合中都存在的元素。
print('set difference_update:')

# 1
s = {"apple", "banana", "cherry"}
sc = {"google", "microsoft", "apple"}
s.difference_update(sc)
print('- s.difference_update(sc): {}'.format(s))

# 2
s = {"apple", "banana", "cherry"}
sc = {"google", "microsoft", "apple"}
sc.difference_update(s)
print('- sc.difference_update(s): {}'.format(sc))


# intersection
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print('s1.intersection(): {}'.format(s1.intersection(s2)))
print('- intersection(s1): {}'.format(s1))
print('- intersection(s2): {}'.format(s2))

# intersection_update
print('set intersection_update():')
r = s1.intersection_update(s2)
print('- intersection_update(s1): {}'.format(s1))
print('- intersection_update(s2): {}'.format(s2))


s1 = {1, 2}
s2 = {1, 2, 4}

# isdisjoint

print('\nisdisjoint():')
x = {"apple", "banana", "cherry"}
y = {"google", "orange", "facebook"}
print('x:{} y:{}'.format(x, y))
print('- x.isdisjoint(y): {}'.format(x.isdisjoint(y)))
print('- y.isdisjoint(x): {}'.format(y.isdisjoint(x)))


# issubset & issuperset
print('\nissubset():')
print('s1:{} s2:{}'.format(s1, s2))
print('- s1.issubset(s2): {}'.format(s1.issubset(s2))) # 判断集合 s1 的所有元素是否都包含在集合 s2 中：T
print('- s2.issubset(s1): {}'.format(s2.issubset(s1))) # 判断集合 s2 的所有元素是否都包含在集合 s1 中：F
print('\nissuperset():')
print('s1:{} s2:{}'.format(s1, s2))
print('- s1.issuperset(s2): {}'.format(s1.issuperset(s2))) # 判断集合 s1 的所有元素是否都包含在集合 s2 中：
print('- s2.issuperset(s1): {}'.format(s2.issuperset(s1))) # 判断集合 s2 的所有元素是否都包含在集合 s1 中：