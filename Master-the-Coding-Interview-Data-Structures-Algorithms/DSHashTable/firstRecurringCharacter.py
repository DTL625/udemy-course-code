#Google Question
#Given an array = [2,5,1,2,3,5,1,2,4]:
#It should return 2

#Given an array = [2,1,1,2,3,5,1,2,4]:
#It should return 1

#Given an array = [2,3,4,5]:
#It should return undefined

def firstRecurringCharacter(input_list :list):
    tmp = []
    for item in input_list:
        if item in tmp:
            return item
        else:
            tmp.append(item)
    return None

def secondRecurringCharacter(input_list :list):
    cnt = 0
    for idx, num in enumerate(input_list):
        for sub_num in input_list[idx + 1:]:
            if num == sub_num:
                return num
    return None

arr = [2,5,1,2,3,5,1,2,4] # 2
rs = firstRecurringCharacter(arr) # O(n)
print(rs) # 2
rs = secondRecurringCharacter(arr) # O(n^2)
print(rs) # 2

# Bonus... What if we had this:
#   [2,5,5,2,3,5,1,2,4]
# return 5 because the pairs are before 2,2
arr = [2,5,5,2,3,5,1,2,4]
rs = firstRecurringCharacter(arr)
print(rs) # 5
rs = secondRecurringCharacter(arr)
print(rs) # 2