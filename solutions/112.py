
def isBouncy(n):
    up, down = False, False
    while n > 9:
        if n % 10 < (n // 10) % 10:
            down = True
        if n % 10 > (n // 10) % 10:
            up = True
        if up == True and down == True:
            return True
        n //= 10
    return False

n = 21780    
bouncy = 0.9 * n

while bouncy != 0.99 * n:
    n += 1
    if isBouncy(n):
        bouncy += 1
        
print(n)


