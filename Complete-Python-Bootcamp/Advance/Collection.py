from collections import Counter;

lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
r = Counter(lst);
print('計算各個數字出現的次數')
print(r)

r = Counter('aabsbsbsbhshhbbsbs')
print('計算各個文字出現的次數')
print(r)

s = 'How many times does each word show up in this sentence word times each each word'
#
r = Counter(s.split())
print('計算各個單字出現的次數')
print(r)

print('計算各個單字出現的次數前兩名')
print(r.most_common(2))
print('或者指定序號')
print(r.most_common()[1:-1])

#
#
c = Counter(s);
print('計算字元總數')
print(sum(c.values()))

print('清除counter')
c.clear() # 清除counter
print(c)

print('轉換成list')
print(list(c))
print('轉換成set')
print(set(c))
print('轉換成dict')
print(dict(c))


c_list = c.items()
print('轉換成list(元素與次數的組合)')
print(c_list)


c += Counter()
print('從list(元素與次數的組合)做轉換')
print(c)
