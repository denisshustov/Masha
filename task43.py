def rev12(list):
    a = list[0]
    b = list[1]
    list[0] = b
    list[1] = a
    return list
print(rev12([6,8,9]))