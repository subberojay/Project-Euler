#includes emptyset in solution
def powerset(s):
    P = []
    x = len(s)
    for i in range(1 << x):
        P.append([s[j] for j in range(x) if (i & (1 << j))])
    return P

#does not include emptyset in solution
def powerset1(s):
    P = []
    x = len(s)
    for i in range(1, 1 << x):
        P.append([s[j] for j in range(x) if (i & (1 << j))])
    return P