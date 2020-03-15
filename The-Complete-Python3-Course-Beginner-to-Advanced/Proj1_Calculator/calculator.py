import re

print("Our magic calculator")
print("type 'exit' to quit\n")


run = True
previous = 0

def performMatch(  ):
    global run, previous
    equation = ''

    if (previous == 0) :
        equation = input('enter equtation: ')
    else:
        equation = input("%s" % (str(previous)))

    if equation == 'quit':
        run = False
    else :
        equation = re.sub('[a-zA-Z, .:()" "]', '', equation)
        include_num = bool(re.search(r'\d', equation))
        if include_num and previous == 0:
            previous = eval(equation) # eval: 計算
            print('result: ', previous)
        elif include_num and previous != 0:
            previous = eval(str(previous) + equation) # eval: 計算
            print('result: ', previous)


while run:
    performMatch();