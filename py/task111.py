i=1
k=0
h=input('ведите чесло ')
d=int(h)

while i<=d:
    print("{0}+{1}={2}".format(k,i,k+i))
    k=k+i    
    i=i+1

print(k)