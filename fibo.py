def fibo(n):
    
    A = (1 + (5 ** 0.5))/ 2
    B = (1 - (5 ** 0.5))/ 2

    return ((A ** n) - (B**n)) / (5 ** 0.5)


n = 6
print(fibo(n))