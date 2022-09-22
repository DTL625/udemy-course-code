# Question: mergeSortedArrays([0,3,4,31], [3,4,6,30]);

# simple
def mergeSortedArrays(arrA: list, arrB:list):
  # sort
  arrA.sort()
  arrB.sort()
  
  # merge
  result = []
  idxA = idxB = 0
  maxA, maxB = len(arrA) - 1 , len(arrB) - 1  

  while (idxA <= maxA) and (idxB <= maxB):
    #print("#", arrA[idxA:], arrB[idxB:])
    # print([idxA, idxB], '-', result, "\n")
    
    if arrA[idxA] > arrB[idxB]:
      result.append(arrB[idxB])
      idxB += 1
    elif arrA[idxA] < arrB[idxB]:
      result.append(arrA[idxA])
      idxA += 1
    else:
      result.append(arrA[idxA])
      result.append(arrB[idxB])
      idxA += 1
      idxB += 1
    print("#", arrA[idxA:], arrB[idxB:])
    print([idxA, idxB], '-', result, "\n")
  # 多一個 待處理
  return result


rs = mergeSortedArrays([4,0,3,29], [6,30,6,3])

print ("\n", rs)