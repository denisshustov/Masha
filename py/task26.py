def getMax (lst):
    max = 0
    i = 0
    while i < len(lst):
        c = lst[i]
        if c > max:
            max = c
        i = i + 1
    return max

list = [65,21,90,57]
m = getMax (list)
print(m)

print(getMax([1,45,6,7,8,99,4,3,155]))