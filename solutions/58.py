
import sympy    
    
n = 49
x = 8

primeCount = 8
diagCount = 13

while primeCount / diagCount > 0.1:
    for i in range(4):
        n += x
        diagCount += 1
        if sympy.isprime(n):
            primeCount += 1
    x += 2

print(x - 1)