
import math

count = 0

for d in range(5, 12001):
    thirdNum = math.floor(d / 3) + 1
    halfNum = math.ceil(d / 2)
    for n in range(thirdNum, halfNum):
        if math.gcd(n, d) == 1:
            count += 1
            
print(count)