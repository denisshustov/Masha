def sumod(list):
    s = 0
    i = 0
    while i < len(list):
        s = s + list[i]
        i = i + 2
    return s
print(sumod([1,2,1,2,1]))