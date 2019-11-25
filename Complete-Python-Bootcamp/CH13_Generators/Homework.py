import random;

def gensquares(N):
    for n in range(N):
        print(n**2, end=' ');
print('problem1 - gensquares:')
gensquares(10)


def rand_num(low, hight, num):
    for n in range(num):
        print(random.randint(low, hight), end=' ')
print('\n prblem2 - rand_num:')
rand_num(1, 10, 12)



print('\n prblem3 - iter:')
s = 'hello'
s = iter(s)
print(list(s));

print('\n prblem3 - iter:')