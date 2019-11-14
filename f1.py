def f3(l,k,m):
    if l or k or not m:
        return True
    else:
        return False

def f2(g,j,d,x):
    g = g + 1
    j = j + 1
    d = d + 1
    x = x + 1
    return g + j + d + x

def f1(g,j,d):
    return g +j + d + '!!!'

o = f1('wg','hg','jk')
print(o)

h = f2(8,9,6,8)
print(h)

print(f3(1>2,True,1==1))
print(f3(2==3,'h'=='j',True))










