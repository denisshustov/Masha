def getmin(a,b):
    if a<b:
        return a
    if a>b:
        return b
    return a

list = [5,78,6,89,3,7,5]
list2 = [7,4,8,1,6,8,67,8]
lenlist = len(list)
lenlist2 = len(list2)

x = 5
y = 9

f = getmin(x,y)
print(f)

z = getmin(x,y)
z1 = getmin(x,100)
z2 = getmin(2,7)
