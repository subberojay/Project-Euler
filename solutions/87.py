
from math import floor

def eratosthenes(n):
    deleted = set()
    k = 2
    while k <= n**0.5:
        if k in deleted:
            k += 1
            continue
        m = k**2
        while m <= n:
            deleted.add(m)
            m += k
        k += 1
    return list(set(range(2, n + 1)) - deleted)

n = 50000000

two = eratosthenes(floor(n**0.5))
three = eratosthenes(floor(n**(1/3)))
four = eratosthenes(floor(n**0.25))

nums = set()

for a in two:
    for b in three:
        for c in four:
            if a**2 + b**3 + c**4 < n:
                nums.add(a**2 + b**3 + c**4)

print(len(nums))