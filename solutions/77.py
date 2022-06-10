
from time import time



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
    return set(range(2, n + 1)) - deleted

primes = eratosthenes(1000)

start = time()

n = 10
nSummations = 5

while nSummations <= 5000:
    n += 1
    nPrimes = [p for p in primes if p <= n]
    primeSums = [0] * (n + 1)
    for i in range(2, n + 1, 2):
        primeSums[i] += 1
    for p in nPrimes[1:]:
        for m in range(n, p + 1, -1):
            for j in range(m - p, 1, -p):
                primeSums[m] += primeSums[j]
        for k in range(p, n + 1, p):
            primeSums[k] += 1
    nSummations = primeSums[n]

print(n)

end = time()
print(end - start)





