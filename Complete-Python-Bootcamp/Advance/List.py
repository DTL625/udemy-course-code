# append()
list = [1, 2, 3]
print('init list:{}'.format(list))
list.append(4)
print('after append:{}'.format(list))
# append() 2
list = [1, 2, 3]
print('init list:{}'.format(list))
list.append([4, 5])
print('after append :{}'.format(list))
# extend()
list = [1, 2, 3]
print('init list:{}'.format(list))
list.extend([4, 5])
print('after extend :{}'.format(list))

# count()
listCheck = [1, 2, 3, 2 ,1 ,1]
print('init listCheck:{}'.format(listCheck))
print('1\'s count :{}'.format(listCheck.count(1)))
print('2\'s count :{}'.format(listCheck.count(2)))
print('3\'s count :{}'.format(listCheck.count(3)))

# index()
list = [1, 3, 2]
print('get index num with key:{}'.format(list.index(3))) # 用于从列表中找出某个值第一个匹配项的索引位置。
# print(list.index(12)) # get error

# insert & pop & remove
list = [1, 2, 3, 4]
print('init list:{}'.format(list))
list.insert(2, 'inserted')
print('after insert:{}'.format(list))
popItem = list.pop(1)
print('list after pop:{}'.format(list))
print('popItem :{}'.format(popItem))
list.remove('inserted')
print('list after remove:{}'.format(list))

# reverse
list = [1, 4, 2, 3]
print('init list:{}'.format(list))
list.reverse()
print('after reserve :{}'.format(list))

# sort
list.sort()
print('after sort :{}'.format(list))
list.sort(reverse=True)
print('after sort(reverse=True):{}'.format(list))

# Be Careful With Assignment
x = [1,2,3]
y = x.append(4)
print('x:{}'.format(x))
print('y:{}'.format(y))

# 必須使用copy()
x = [1,2,3]
y = x.copy()
y.append(4)
print('x:{}'.format(x))
print('y:{}'.format(y))