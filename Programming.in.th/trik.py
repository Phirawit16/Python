swap = input()

a=1
b=0
c=0
d=0

for i in swap:
    if i =="A":
        d=a
        a=b
        b=d
    elif i=="B":
        d=b
        b=c
        c=d
    elif i =="C":
        d=c
        c=a
        a=d
if a == 1:
    print("1")
elif b == 1:
    print("2")
elif c == 1:
    print("3")