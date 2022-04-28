class MyArray:
  data = list()
  def __init__(self):
    pass
  def get(self, index):
    pass
  def push(self, item):
    self.data.append(item)
    # 等同於 self.data[len(self.data):] = [item]
    pass
  def pop(self):
    self.data.pop()
    # 等同於 del(self.data[len(self.data) - 1])
    pass
  def deleteAtIndex(self, index):
    self.shiftItems(index)
    pass
  def shiftItems(self, index):
    for idx in range(index, len(self.data) - 1):
      self.data[idx] = self.data[idx + 1]
    del(self.data[len(self.data) - 1])

    pass

myArray = MyArray()
myArray.push('hi')
myArray.push('you')
myArray.push('!')
myArray.pop()
myArray.deleteAtIndex(0)
myArray.push('are')
myArray.push('nice')
myArray.shiftItems(0)
print(myArray.data)