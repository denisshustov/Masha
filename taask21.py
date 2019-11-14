print('q - exit')
jo=0
k=[]
while 0==0:
    h=input('веди чесло')
    if h=='q':
        break
    k.append(int(h))

p=123
sum=0
m=0
while m<len(k):
    sum=sum+k[m]
    m=m+1
print(sum)