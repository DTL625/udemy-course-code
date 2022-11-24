class HashTable:
    def __init__(self, size):
        self.table = [None] * size

    def _hash(self, key):
        res = 0
        for i in range(len(key)):
            res = (res + ord(key[i])) % len(self.table)
        # print('key: {}, hash:{}'.format(key, res))
        return res

    def set(self, key, value):
        self.table[self._hash(key)] = [key, value]

    def get(self, key):
        return self.table[self._hash(key)]

    """
      ch83 keys()章節 
    """

    def keys(self):
        output = []
        # self.table.items()
        for obj in self.table:
          if obj is not None:
            output.append(obj[0])
        return output

hashTb = HashTable(size=50)
hashTb.set('grape', 100)
hashTb.set('apple', 50)
hashTb.set('orange', 70)

print(hashTb.get('grape'))
print(hashTb.get('apple'))
print(hashTb.get('orange'))
print(hashTb.keys())
