d = []
total = 0
while len(d) != 9:
    hatnumber = int(input())
    if hatnumber not in d:
        d.append(hatnumber)
        total += hatnumber
for i in range(len(d)):
    for j in range(len(d)):
       if total - 100 == d[i] + d[j]:
           for k in range(len(d)):
               if k == i or k == j:
                   continue
               else:
                   print(d[k])