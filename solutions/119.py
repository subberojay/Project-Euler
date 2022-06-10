
#Checks all x^n up to a capped integer (set to 100) for this property.
#Once all x^n up to the cap have been checked, the cap is multiplied by 10
#and the search continues. Terminates once 30 valid solutions have been found
#and returns the 30th. C

def digitsum(n):
    x = 0
    for i in range(len(str(n))):
        x += n % 10
        n //= 10
    return x

bases = [0, 1]
cap = 100
valid = []

while len(valid) < 30:
    for n in range(2, len(str(cap)) * 9):
        if n >= len(bases):
            bases.append(n**2)
        while bases[n] < cap:
            if digitsum(bases[n]) == n:
                valid.append(bases[n])
            bases[n] *= n
    cap *= 10

print(valid[29])

            


