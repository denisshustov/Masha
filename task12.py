print('ведите количество слагаемых')
maxnum = input()
sum = 0
g = 0
k=''
while g < int(maxnum):
    print('ведите чесло')
    num = input()
    k=k+num
    if(g+1 != int(maxnum)):
        k=k+'+'
    sum = sum + int(num)
    g = g + 1
print('результат' + str(sum))
print(k)