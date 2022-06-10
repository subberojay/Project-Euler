

tri = [n*(n + 1) // 2 for n in range(45, 141)]
squ = [n**2 for n in range(32, 100)]
pent = [n*(3*n - 1) // 2 for n in range(26, 82)]
hexa = [n*(2*n - 1) for n in range(23, 71)]
hept = [n*(5*n - 3) // 2 for n in range(21, 64)]
octa = [n*(3*n - 2) for n in range(19, 59)]

nums = {}

for n in tri:
    try:
        nums[n].add(3)
    except KeyError:
        nums[n] = {3}

for n in squ:
    try:
        nums[n].add(4)
    except KeyError:
        nums[n] = {4}

for n in pent:
    try:
        nums[n].add(5)
    except KeyError:
        nums[n] = {5}

for n in hexa:
    try:
        nums[n].add(6)
    except KeyError:
        nums[n] = {6}

for n in hept:
    try:
        nums[n].add(7)
    except KeyError:
        nums[n] = {7}

def avail(digits, visited):
    l = [x for x in nums if digits * 100 <= x and x < (digits + 1) * 100 and nums[x].difference(visited) != set()]
    return [(n, nums[n]) for n in l]

def steps(chain):
    new_chains = []
    for node in avail(chain[0][-1] % 100, chain[1]):
        for k in node[1].difference(chain[1]):
            new_chains.append((chain[0] + [node[0]], chain[1].union({k})))
    return new_chains
            
for x in octa:
    c = [([x], set())]
    for i in range(5):
        new_chains = []
        for chain in c:
            new_chains += steps(chain)
        c = new_chains
    for chain in new_chains:
        if chain[0][0] // 100 == chain[0][-1] % 100:
            print(sum(chain[0]))



