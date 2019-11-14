#x y z
#x+y=4
#x+z=10
#y+z=8

x=0
y=0
z=0
max=10
while x<=max:
    y=0
    while y<=max:
        z=0
        while z<=max:
            if x+y==4  and x+z==10 and y+z==8:
                print(x)
                print(y)
                print(z)
            z=z+1
        y=y+1
    x=x+1




