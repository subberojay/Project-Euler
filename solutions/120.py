
rMaxSum = 0

for a in range(3, 1001):
    k = a**2
    x, y = a - 1, a + 1
    xCycle, yCycle = [x], [y]
    xFlag, yFlag = True, True
    while xFlag or yFlag:
        xCycle.append((x * xCycle[-1]) % k)
        yCycle.append((y * yCycle[-1]) % k)
        if xCycle[-1] == 1:
            xFlag = False
        if yCycle[-1] == 1:
            yFlag = False
    rMaxSum += max([(x + y) % k for x, y in zip(xCycle, yCycle)])
    
print(rMaxSum)
            
