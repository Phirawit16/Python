number = [int(i) for i in input().split()]
modula = []
for i in range(min(number)):
    if (number[0] % (i+1)) == 0 and (number[1] % (i+1)) == 0:
        modula.append(i+1)
print(max(modula))
