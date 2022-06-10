
def digitsum(n):
    x = 0
    for i in range(len(str(n))):
        x += n % 10
        n //= 10
    return x