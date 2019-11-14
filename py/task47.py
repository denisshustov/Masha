def rev(list):
    if len (list) < 6:
        print('error')
        return []
    a = list[4]
    b = list[6]
    list[4] = b
    list[6] = a
    return list
print(rev([76,9,67,5,76,65,89]))