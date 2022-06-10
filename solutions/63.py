
nPowers = 1

for x in range(2, 10):
    n = 1
    while len(str(x**n)) >= n:
        if len(str(x**n)) == n:
            nPowers += 1
        n += 1
        
print(nPowers)