def revprint(list):
    size = len(list)
    i = size - 1
    while i >= 0:
        print(list[i])
        i = i - 1

revprint([1,2,3,4])