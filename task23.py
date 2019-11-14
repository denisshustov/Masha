list=[66,6,68,99,4,8,7]
print(list)

listlen = len(list)
i = 0
j=0
while i<listlen:
    if i+1<listlen:
        ce1 = list[i] 
        ce2 = list[i+1]
        if ce1 > ce2:
            tmp = ce1
            list[i] = ce2
            list[i+1] = tmp
        i = i+1
    else:
        i=0

    j=j+1
    if j>50:
        break
    

print(list)