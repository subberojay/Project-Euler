
from sympy import isprime

n, m = 1, 2
while n * m <= 1000000:
    n *= m
    m += 1
    while isprime(m) is False:
        m += 1
print(n)