names = ['Paul', 'Bob', 'Jim', 'Nathan']

for name in names:
    if len(name) > 4 and ('n' in name or 'N' in name):
        print(name + ' has ' + str(len(name)) + ' letters')
else:
    while len(names) > 0:
        names.pop()
        print(names)
    print('No more names!')
