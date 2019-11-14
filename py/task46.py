def rev(list):
    if len (list) < 5:
        print('error')
        return []
    a = list[1]
    b = list[5]
    list[1] = b
    list[5] = a
    return list
print(rev([2,8,4,8]))