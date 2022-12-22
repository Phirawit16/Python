a1 = [int(i) for i in input().split()]
a1.sort()
A = [str(i) for i in input()]
B = A.copy()
B.sort()

for i in A:
    if i == "A":
        print(a1[0],end=" ")
    elif i == "B":
        print(a1[1],end=" ")
    else:
        print(a1[2],end=" ")