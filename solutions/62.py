
n = 346
cubeDigits = {}

while True:
    digits = tuple(sorted(str(n**3)))
    if digits in cubeDigits:
        cubeDigits[digits].add(n**3)
        if len(cubeDigits[digits]) == 5:
            break
    else:
        cubeDigits[digits] = {n**3}
    n += 1
    
print(min(cubeDigits[tuple(sorted(str(n**3)))]))