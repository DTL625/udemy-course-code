from colorama import Fore, Style

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print(Fore.RED + 'you get a type error with operate')


# --------------------

try:
    x = 5
    y = 0

    z = x/y
except:
    print('you get a ZeroDivisionError ')
finally:
    print(Fore.LIGHTGREEN_EX + 'all done')

# --------------------

def ask():
    while 1:
        try:
            inp = int(input(Fore.BLUE + 'In put an integer:'))
        except:
            print(Fore.RED + 'An error occurred! Please try again!')
            continue
        else:
            print(Fore.LIGHTGREEN_EX + 'Thank you, your number squared is:' + str(inp));
            break

ask()
