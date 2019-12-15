import re;
#
# List of patterns to search for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

r = re.search('hello', 'hello world')
# print(r) # <re.Match object; span=(0, 5), match='hello'>

r = re.search('hola', 'hello world')
# print(r) # none


for pattern in patterns:
    print('Searching for "%s" in:\n "%s"\n' %(pattern, text))

    #Check for match
    if re.search(pattern,text):
        print('Match was found. \n')
    else:
        print('No Match was found.\n')

match = re.search(patterns[0], text)
print(type(match))
print(match.start())
print(match.end())

match = re.search(patterns[1], text)
print(type(match))
print(match.start())
print(match.end())
def multi_re_find(patterns, phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' % (pattern))
        print(re.findall(pattern, phrase))
        print('\n')


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [
    'sd*',  # s followed by zero or more d's
    'sd+',  # s followed by one or more d's
    'sd?',  # s followed by zero or one d's
    'sd{3}',  # s followed by three d's
    'sd{2,3}',  # s followed by two to three d's
]

multi_re_find(test_patterns, test_phrase)


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [
    '[sd]',  # either s or d
    's[sd]+'  # s followed by one or more s or d
]

multi_re_find(test_patterns, test_phrase)

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

r = re.findall('[^!.? ]+', test_phrase)
print(r)

