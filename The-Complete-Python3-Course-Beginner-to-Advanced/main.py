import re

string = " 'I'M NOT YELLING', she said. though we knew it to not be true."
print(string)

new = re.sub('[A-Z]', '', string)
print(new)