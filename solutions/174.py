

n = 1000000

cap = (n + 4) // 4

base = 3

ls = [0] * (n + 1)

while base < cap:
    l = base
    x = 4 * l - 4
    while x <= n:
        ls[x] += 1
        l += 2
        x += 4 * l - 4
    base += 1
    
ls[4 * cap - 4] += 1

count = 0

for c in ls:
    if 1 <= c <= 10:
        count += 1
        
print(count)

