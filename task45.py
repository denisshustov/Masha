def rev2(list):
    if len (list) < 3:
        print('error')
        return []
    a = list[0]
    b = list[2]
    list[0] = b
    list[2] = a
    return list
print(rev2([1,2,7,3,4]))