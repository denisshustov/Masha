print(' выберете знак + - *')
op=input()

print('ведите первое чесло')
sd1=input()

print('ведите первое чесло')
sd2=input()

result=0

if op=='+':
    result = int(sd1) + int(sd2)

if op=='-':
    result = int(sd1) - int(sd2)

if op=='*':
    result = int(sd1) * int(sd2)
print('результат ='+ str(result))
