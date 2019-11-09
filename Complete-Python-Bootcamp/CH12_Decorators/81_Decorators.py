# def say_hi(name = 'Jose'):
#     print('hello ' + name);
#
# say_hi(name = 'Sean')    # hello Sean
# print(say_hi)            # <function hello at 0x10de671e0>
# greet = say_hi           # 此時greet會複製一份say_hi
# print(greet)             # <function hello at 0x10de671e0>
#
# del say_hi
# print(say_hi)            # NameError: name 'hello' is not defined
# print(greet)             # 無法執行下去

# ----- div -----

# def hello(name = 'Jose'):
#     print('The hello() function has been executed')
#
#     def greet():
#         return '\t This is inside the greet() function'
#
#     def welcome():
#         return "\t This is inside the welcome() function"
#
#     print(greet())
#     print(welcome())
#     print("Now we are back inside the hello() function")
#
# hello(name = 'Sean')    # 外部調用父方法，子方法也會跟著執行
# welcome()               # 外部無法直接調用子方法

# ----- div -----

def say_hello(name='Jose'):
    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    if name == 'Jose':
        return greet
    else:
        return welcome

say_somthing = say_hello('Jose')
# print(say_somthing())

say_somthing = say_hello('Sean')
# print(say_somthing())

# ----- div -----

def hello():
    return 'hello! pythoner'

def hola():
    return 'hola! pythoner'

def say_something(func_name):
    print(func_name())

# say_something(hello)    # hello! pythoner
# say_something(hola)     # hola! pythoner

# ----- div -----

def new_decorator(origin_func):

    def wrap_func():
        print('before origin function')
        origin_func()
        print('after origin function')

    return wrap_func


def func_needs_decorator():
    print('I want to be decorated!!!')


func_needs_decorator()
decoratred_func = new_decorator(func_needs_decorator);
decoratred_func()

@new_decorator
def func_needs_decorator_with_at():
    print('I want to be decorated!!!')
func_needs_decorator_with_at()