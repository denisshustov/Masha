names = []
p = 0
while p<2:
    cat = input('веди имя')
    names.append(cat)
    p = p + 1
p = len(names)-1
while p>=0:
    print('привет' + ' ' + names[p])
    p = p - 1