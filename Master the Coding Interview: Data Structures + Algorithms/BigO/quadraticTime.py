boxes = ['a', 'b', 'c', 'd', 'e']

def logAllPairsOfArray(arr: list):
  for main_arr in arr:
    for sub_arr in arr:
      print('{} {}'.format(main_arr, sub_arr))

logAllPairsOfArray(boxes) # O(n * n) => O(n^2)