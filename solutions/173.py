

n = 1000000

cap = (n + 4) // 4

base = 3

count = 0

while base < cap:
    l = base
    x = 4 * l - 4
    while x <= n:
        count += 1
        l += 2
        x += 4 * l - 4
    base += 1
    
print(count + 1)
    
    