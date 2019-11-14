def getmax(lst):

    max = 0
    i = 0
    while i < len(lst):
        if lst[i] > max:
            max = lst[i]
        i = i + 1
    return max

print(getmax([67,98,14,6,91]))
print(getmax([1,1,1,1,2,3,4,12]))
    







