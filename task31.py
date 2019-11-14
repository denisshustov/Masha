def getsyu(array):
    sum = 0
    i = 0
    while i < len(array):
        j = array[i]
        sum = sum + j
        i = i + 1
    return sum
r = getsyu([56,78,3,90])