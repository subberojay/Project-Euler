
def ispandigital(m):
    if len(str(m)) != 9:
        return False
    digits = [0] * 10
    for c in str(m):
        digits[int(c)] += 1
    if digits[0] != 0 or 0 in digits[1:]:
        return False
    return True
    
def con_product(k, n):
    x = ''
    for m in range(1, n + 1):
        x += str(k * m)
    return int(x)

pandigitals = [123456789]

k = 2

while con_product(k, 2) < 1000000000:
    n = 2
    while con_product(k, n) < 1000000000:
        if ispandigital(con_product(k, n)):
            pandigitals.append(con_product(k, n))
        n += 1
    k += 1
    
print(max(pandigitals))
    