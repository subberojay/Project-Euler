
triples = {}

def factors(n):
    return [
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    ]
    
for r in range(2, 325001, 2):
    facs = factors(r**2 // 2)
    for i in range(0, len(facs), 2):
        wire = 3*r + 2*facs[i] + 2*facs[i + 1]
        try:
            triples[wire].add(tuple(sorted([r + facs[i], r + facs[i + 1],
                                      r + facs[i] + facs[i + 1]])))
        except KeyError:
            if wire <= 1500000:
                triples[wire] = {tuple(sorted([r + facs[i], r + facs[i + 1],
                                         r + facs[i] + facs[i + 1]]))}
            else:
                continue
    
print(len([x for x in triples if len(triples[x]) == 1]))