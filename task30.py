def getmin(array):
    min = 100
    i = 0
    while i < len(array):
        if array[i] < min:
            min = array[i]
        i = i + 1
    return min
print(getmin([1,2,3,4,5,6]))