all = []
while True :
    num = int(input())
    if num < 0:
        print("End")
        break
    all.append(num)
print(all)
all.sort()
print(all)
print("min is ",min(all))
print("max is ",max(all))