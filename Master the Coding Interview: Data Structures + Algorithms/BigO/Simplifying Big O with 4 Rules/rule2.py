import math

def printFirstItemThenFirstHalfThenSayHi100Times(times: list):
  print(times[0])  #O(1)

  midIndex = math.floor(len(times)/ 2)
  index = 0

  while(index < midIndex):
    print(times[index]) # O(n/2)
    index += 1

  for i in range(100):
    print('hi' + str(i)) # O(100)
  
printFirstItemThenFirstHalfThenSayHi100Times([1,2,3,4,5])