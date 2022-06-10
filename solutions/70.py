
from sympy import totient

x = 87109

m = x / totient(x) 

for n in range(1, 10**7):
    if sorted(str(n)) == sorted(str(totient(n))) and n / totient(n) < m:
        x = n
        m = x / totient(x)