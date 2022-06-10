
def isprime(n):
    if n == 1:
        return False
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    
import itertools

no_primes = True
n = 9

while no_primes is True:
    pandigitals = [x for x in itertools.permutations(list(range(n, 0, -1)))]
    for p in pandigitals:
        m = 0
        for d in range(len(p)):
            m += p[d] * 10**(n - d - 1)
        if isprime(m):
            no_primes = False
            print(m)
        if no_primes is False:
            break
    n -= 1
