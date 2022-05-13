'''
影片連結：https://www.youtube.com/watch

提供一個列表與總數，找出在列表中將各元素相加後是否有等於該數值的組合。

例：

1.
    list = [1, 2, 3, 9]
    sum  = 8

    return false

2.

    list = [1, 2, 4, 4]
    sum  = 8

    return true
'''

import numpy
import time


def hasPairWithSum(listA, sum):
    for idx, item in enumerate(listA):
        if (len(listA) - 1) <= idx:
            break
        for sub_item in listA[idx + 1:]:
            if (item + sub_item) is sum:
                print(item, '+', sub_item, '=', sum)
                return True
    return False

def hasPairWithSumB(listA: list, sum):
    listRes = list();
    for item in listA:
        idx = sum - item
        if idx in listRes:
            return True
        else:
            listRes.append(idx)

    return False


listA = numpy.random.randint(1, 100, size=10000).tolist()
print(listA)
sum = numpy.random.randint(100, 200, size=1)

if __name__ == '__main__':
    start_time = time.time()
    # print('list: ', listB)
    # print('sum: ', sum)
    print(hasPairWithSum(listA, sum))
    print("--- %s seconds ---" % (time.time() - start_time))
    print(hasPairWithSumB(listA, sum))
    print("--- %s seconds ---" % (time.time() - start_time))