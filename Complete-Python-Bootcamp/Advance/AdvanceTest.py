num = 1024
print(hex(num))

num = 5.23222
print(round(num, 2))

s = 'hello how are you Mary, are you feeling okay?'
print(s.lower())

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))


set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
# Find the elements in set1 that are not in set2
res = set1.intersection(set2)
print(res)

res = {x: x**3 for x in range(5)}
print(res)

list1 = [1,2,3,4]
list1.reverse()
print(list1)


list2 = [3,4,2,5,1]
list2.sort()
print(list2)