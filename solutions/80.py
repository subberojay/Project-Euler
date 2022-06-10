
from decimal import Decimal, getcontext

total = 0

getcontext().prec = 102

for n in range(1, 100):
    if n**0.5 == int(n**0.5):
        continue
    digits = str(Decimal(n)** Decimal(0.5))
    total += sum([int(d) for d in digits[:101] if d != '.'])
    
print(total)