
from time import time

a = time()

import numpy as np

n = 2
partitions = np.ones((2, 2), dtype=int)
partitions[-1, -1] = 2

while partitions[-1, -1] % 1000 != 0:
    n += 1
    newTable = np.ones((n, n), dtype=int)
    newTable[:n - 1, :n - 1] = partitions
    newTable[:n - 1, -1] = newTable[:n - 1, -2]
    for i in range(1, n - 1):
        newTable[-1, i] = newTable[-1, i - 1] + newTable[-(i + 2), i]
    newTable[-1, -1] += newTable[-1, -2]
    partitions = newTable
  
print(n)

b = time()

print(b - a)  

a = time()

def partitions(p):
    if p == 1 or p == 2 or p == 3:
        return p
    partitions = [1] * p
    for n in range(2, p):
        partitions[n - 1] += 1
        for i in range(n, p):
            partitions[i] += partitions[i - n]
    return partitions[-1] + 1

n = 2

while partitions(n) % 1000 != 0:
    n += 1

print(n)
    
b = time()

print(b - a)   
    
    
    
    
    
    
    
    