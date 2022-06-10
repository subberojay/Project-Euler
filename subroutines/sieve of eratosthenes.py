
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
    