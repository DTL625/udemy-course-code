
def compareTwoBoxsTwice(box: list, box2:list):
  for item in box:
    print(item) # O(n)

  for item in box2:
    print(item) # O(m)


compareTwoBoxsTwice([1, 3, 5], [2, 4, 6]) #O(n + m)