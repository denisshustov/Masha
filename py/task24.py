list = [5,76,8,2,7,67,98,76]
i = 0
while i<len(list):
    q = list[i] % 2
    if q==0:
        print(list[i])
    i = i + 1