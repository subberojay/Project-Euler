from time import time

start = time()

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

primes = eratosthenes(10000)
primes = sorted([p for p in primes if p >= 1000])
stringPrimes = [sorted(str(p)) for p in primes]
permPrimes = [p for p in primes if stringPrimes.count(sorted(str(p))) >= 3]
permFamilies = dict()

for p in permPrimes:
    if tuple(sorted(str(p))) in permFamilies:
        permFamilies[tuple(sorted(str(p)))].append(p)
    else:
        permFamilies[tuple(sorted(str(p)))] = [p]

for family in permFamilies:
    f = permFamilies[family]
    for i in range(len(f[:-2])):
        for j in range(i + 1, len(f[:-1])):
            if f[j] + (f[j] - f[i]) in f:
                print(str(f[i]) + str(f[j]) + str(f[j] + (f[j] - f[i])))
                
end = time()
print(end - start)
