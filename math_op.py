print('выберете действие + -')
op=input()

print('ведите первае чесло')
sd1=input()

print('ведите второе чесло')
sd2=input()
result=0

if op=='+':
    result = int(sd1) + int(sd2)

if op=='-':
    result = int(sd1) - int(sd2)

print("Результат: {1}{2}{3}={0}".format(result, sd1, op, sd2 ))
































