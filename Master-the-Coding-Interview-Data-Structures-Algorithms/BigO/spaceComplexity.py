# Space complexity O(1)
def boo(n) :
  for i in n:
    print('boo')
boo([1,2,3,4,5])

# Space complexity O(n)
def arrayOfHiNTimes(n: int):
  hiArray = []
  for i in range(n):
    hiArray.append('hi')
    # do not use this
    # hiArray = hiArray.append('hi')
  return hiArray
arrayOfHiNTimes(6)