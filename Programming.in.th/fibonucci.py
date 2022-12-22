def fibo(start):
    if start <= 1:
        return start
    else:
        x = fibo(start-1)+fibo(start-2)
        return x 
for i in range(8):
    print(fibo(i))