modula = set()
for i in range(10):
    number = int(input())
    y = number % 42
    modula.add(y)
x = 0
for item in modula:
    x += 1
print(x)
