'''
Given 2 arrays, create a function that let's a user know (`true`/`false`) whether these two arrays contain any common items
For Example:
```javascript
const array1 = ['a', 'b', 'c', 'x'];
const array2 = ['z', 'y', 'i'];
```
should return `false`.

```javascript
const array1 = ['a', 'b', 'c', 'x'];
const array2 = ['z', 'y', 'x'];
```
should return `true`.

hints:
 - 2 parameters
 - arrays
 - no size limit
 - return true or false
'''

arrayA = ['a', 'b', 'c', 'x', 'b']
arrayB = ['z', 'y', 'i']

arrayC = ['a', 'b', 'c', 'x']
arrayD = ['z', 'y', 'x']

def gotCommonItemsA(inputA, inputB):
    for itemA in inputA:
        for itemB in inputB:
            if itemA is itemB:
                return True
    return False

def gotCommonItemsB(inputA, inputB):
    for itemA in inputA:
        if itemA in inputB:
            return True
    return False


def gotCommonItemsC(inputA: list, inputB: list):
    for itemA in inputA:
        if inputB.count(itemA) > 0:
            return True
    return False

if __name__ == '__main__':
    print("輸入參數")
    print(arrayA)
    print(arrayB)
    print(arrayC)
    print(arrayD)

    print("# 執行 gotCommonItemsA(雙for迴圈) 輸出結果")
    print(gotCommonItemsA(arrayA, arrayB)) # false
    print(gotCommonItemsA(arrayC, arrayD)) # true

    print("# 執行 gotCommonItemsB(python in方法) 輸出結果")
    print(gotCommonItemsB(arrayA, arrayB)) # false
    print(gotCommonItemsB(arrayC, arrayD)) # true

    print("# 執行 gotCommonItemsC(python list.count方法) 輸出結果")
    print(gotCommonItemsC(arrayA, arrayB)) # false
    print(gotCommonItemsC(arrayC, arrayD)) # true
