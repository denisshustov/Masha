i=[5,97,5,98]
l=[]
sum=0
u=0
while u<len(i):
    sum=sum+i[u]
    print(i[u])
    l.append(u)
    u=u+1
print(sum)