"""
m,n = [int(i) for i in input().split()]
mat1 = []
mat2 = []
mat3 = []
for i in range(m):
    mat1.append(input().split())
for i in range(m):
    mat2.append(input().split())
for i in range(m):
    mat3.append([])
    for k in range(n):
        mat3[i].append(int(mat1[i][k]) + int(mat2[i][k]))
for i in mat3:
    for x in i:
        print(x,end=" ")
    print("")
"""
m,n = [int(i) for i in input().split()]
mt1 = []
mt2 = []
mt3 = []
for row in range(m):
    mt1.append(input().split())
for row in range(m):
    mt2.append(input().split())
for row in range(m):
    mt3.append([])
    for column in range(n):
        mt3[row].append(int(mt1[row][column]) + int(mt2[row][column]))
for row in mt3:
    for column in row:
        print(column,end=" ")
    print(" ")