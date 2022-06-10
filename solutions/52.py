
n = 1
k = 2
while k <= 7:
    if len(str(n)) == len(str(k * n)):
        if sorted(str(n)) == sorted(str(k * n)):
            k += 1
        else:
            k = 2
            n += 1
    else:
        k = 2
        n += 1
print(n)