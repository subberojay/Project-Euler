
def partitions(p):
    if p == 1 or p == 2 or p == 3:
        return p
    partitions = [1] * p
    for n in range(2, p):
        partitions[n - 1] += 1
        for i in range(n, p):
            partitions[i] += partitions[i - n]
    return partitions[-1] + 1

