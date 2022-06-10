
from time import time

start = time()

import math


closest = [(2, 5), (3 / 7 - 2 / 5)]


for d in range(8, 1000001):
    n = math.floor(d * (3 / 7))
    if math.gcd(n, d) == 1:
        diff = 3 / 7 - n / d
        if diff < closest[1]:
            closest = [(n, d), diff]
    
print(closest[0][0])



end = time()

print(end - start)