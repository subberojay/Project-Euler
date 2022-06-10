
from decimal import Decimal, getcontext

getcontext().prec = 100

sol = 0
bigx = 0

for D in range(2, 1000):
    if D**0.5 == int(D**0.5):
        continue
    f = Decimal(D).sqrt()
    h, k, a = [1, int(f)], [0, 1], [int(f)]
    while h[-1]**2 - D*k[-1]**2 != 1:
        f = 1 / (f - a[-1])
        a.append(int(f))
        h.append(a[-1]*h[-1] + h[-2])
        k.append(a[-1]*k[-1] + k[-2])
    if h[-1] > bigx:
        bigx = h[-1]
        sol = D

print(sol)
        
              
    
    
        
        
        