try:
    result = 10 + '10'
except:
    print ('get err')
else:
    print('get well')

# ########################################

try:
    f = open('foo_file', 'r')
    f.write('Write a test file')
except TypeError:
    print('get a type-error')
except OSError:
    print('get a os-error')
finally:
    print('i always run')

# ########################################

try:
    f = open('foo_file', 'r')
    f.write('Write a test file')
except:
    print('All other except!')
finally:
    print('i always run')

########################################

def ask_for_int():

    while 1:
        try:
            res = int(input('plz input a num:'))
        except:
            print('not a int number')
            continue
        else:
            print('yes thank you')
            break
        finally:
            print('is end of except/else/finally')

ask_for_int()