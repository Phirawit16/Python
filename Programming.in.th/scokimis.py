position = [int(i) for i in input().split()]
position.sort()
if (position[2] - position[1]) > (position[1] - position[0]):
    print(position[2] - position[1] - 1)
elif (position[1] - position[0]) >= (position[2] - position[1]):
    print(position[1] - position[0] - 1)
else:
    print(0)
