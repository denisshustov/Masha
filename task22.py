list=[3,5,6,7,8,9,33,4,5,1,12,14,15,88,65,3,]
ren=0
while ren<len(list):
    i=list[ren]
    if (i%2==0 and i<10 )or (i%2!=0 and i>10):
        print(i)
    
    ren=ren+1
    


