

def isprime(n):
    if n == 1:
        return False
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    
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

    
def powerset1(s):
    P = []
    x = len(s)
    for i in range(1, 1 << x):
        P.append([s[j] for j in range(x) if (i & (1 << j))])
    return P
    
x = 56004

primes = eratosthenes(1000000)

b = False

while b is False:
    if x in primes:
        for n in {'0', '1', '2'}.intersection(set(str(x)[:-1])):
            indices = [i for i in range(len(str(x))) if str(x)[i] == n]
            indexSubsets = powerset1(indices)
            for s in indexSubsets:
                y = x
                primeCount = 1
                nonPrimeCount = int(n)
                while nonPrimeCount < 3 and primeCount < 8:
                    for i in s:
                        y += 10**(len(str(x)) - (i + 1))
                    if y in primes:
                        primeCount += 1
                    else:
                        nonPrimeCount += 1
                if primeCount == 8:
                    print(x)
                    print(s)
                    b = True
    x += 1
                        
                        
                        
                        
                        
                        