from time import time

a = time()

from fractions import Fraction as Frac

numeratorCount = 0
i = 0
f = Frac(1, 2)

while i < 1000:
    rootTwoFrac = 1 + f
    if len(str(rootTwoFrac.numerator)) > len(str(rootTwoFrac.denominator)):
        numeratorCount += 1
    f = Frac(1, 2 + f)
    i += 1

print(numeratorCount)

b = time()

print(b - a)