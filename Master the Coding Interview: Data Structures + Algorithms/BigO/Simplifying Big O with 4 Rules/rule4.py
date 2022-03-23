def printAllNumbersThenAllPairSums(arr: list):
  print('these are the numbers:')
  for item in arr:
    print(item)  # O(n)
  
  print('and these are their sums:');
  for main_arr in arr:
    for sub_arr in arr:
      print(main_arr + sub_arr) # O(n^2)

printAllNumbersThenAllPairSums([1, 2, 3, 4, 5]) # O(n + n^2 ) => O(n^2)