
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

print('sieve complete')

primes = list(eratosthenes(10**6))
primes.sort()

n, remainder = 7037, 0

while remainder <= 10**10:
    n += 1
    x0, y0, k = primes[n - 1] - 1, primes[n - 1] + 1, primes[n - 1]**2
    x, y = primes[n - 1] - 1, primes[n - 1] + 1
    for i in range(n - 1):
        x = (x * x0) % k
        y = (y * y0) % k
    remainder = (x + y) % k
    
print(n)
    

