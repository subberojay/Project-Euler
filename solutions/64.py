
from decimal import Decimal, getcontext

getcontext().prec = 300

oddPeriod = 0

for D in range(2, 10000):
    if D**0.5 == int(D**0.5):
        continue
    f = Decimal(D).sqrt()
    ratios = [str(f)[:10]]
    while True is True:
        f = 1 / (f - int(f))
        if str(f)[:10] in ratios:
            break
        ratios.append(str(f)[:10])
    if (len(ratios) - 1) % 2 == 1:
        oddPeriod += 1

print(oddPeriod)