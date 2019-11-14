f=int(input())
if f>100:
    print('большое чело!!!')
if f<100:
    print('маленькое чесло!!!')
u=1
while u<f:
    print(str(u)+'+'+str(f-u))
    u=u+1