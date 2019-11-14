print('ведите количества слагаимых чисел')
count=input()

sum=0
n=0
while n<int(count):
    print('ведите чесло')
    t=input()
    sum=sum+int(t)    
    n=n+1


print(sum)