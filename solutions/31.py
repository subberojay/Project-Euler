

coin_vals = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

def coin_sum(x):
    sums = [1] * (x + 1)
    coins = [c for c in coin_vals if c <= x]
    for v in coins[1:]:
        sums[v] += 1
        for i in range(v + 1, x + 1):
            sums[i] += sums[i - v]
    return sums[x]
    