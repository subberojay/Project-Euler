
from fractions import Fraction as frac

vals = [1, 2]

for i in range(4, 101):
    if i % 3 == 0:
        vals.append(vals[i - 5] + 2)
    else:
        vals.append(1)
        
vals.reverse()
convergent = frac(0, 1)

for x in vals:
    convergent += x
    convergent = frac(1, convergent)

convergent += 2

print(sum([int(d) for d in str(convergent.numerator)]))