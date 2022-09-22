## Rule1 - Worst Case

everyone = ['James', 'Robert', 'John', 'Michael', 'nemo', 'William', 'David', 'Richard', 'Joseph', 'Thomas']

print("===在集合中尋找nemo===")
for (num, name) in enumerate(everyone):
    print('running ' + str(num))
    if name == 'nemo':
        print('found nemo!')



everyone = ['James', 'Robert', 'John', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'nemo']

print("\n===在集合中尋找nemo(最差情況)===")
for (num, name) in enumerate(everyone):
    print('running ' + str(num))
    if name == 'nemo':
        print('found nemo!')
