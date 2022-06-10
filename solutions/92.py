
def squareDigitSum(n):
    s = 0
    while n:
        s += (n % 10)**2
        n //= 10
    return s

one, eightyNine = {1}, {89}

for n in range(2, 568):
    chain = {n}
    while n not in one and n not in eightyNine:
        n = squareDigitSum(n)
        chain.add(n)
    if n in one:
        one = one.union(chain)
    else:
        eightyNine = eightyNine.union(chain)
        
oneCount, eightyNineCount = len(one), len(eightyNine)

for n in range(568, 10000000):
    m = squareDigitSum(n)
    if m in one:
        oneCount += 1
    else:
        eightyNineCount += 1
        
print(eightyNineCount)
    