list = [45,90,21,67]
max = 0
min = 1000
i = 0  
while i<len(list):
    c = list[i]
    if c<min:
        min = c
    if c>max:
        max = c
    i = i + 1
print(min)
print(max)