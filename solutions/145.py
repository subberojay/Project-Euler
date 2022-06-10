
import time

def revCount(N):
    count = 0
    for n in range(1, N):
        nRev = int(str(n)[::-1])
        m = n + nRev
        even = False
        while m // 10 > 0:
            if (m % 10) % 2 == 0:
                even = True
                break
            m //= 10
        if even == False:
            count += 1
    return count


N = 1000
a = time.time()
print(revCount(N)) 
b = time.time()
print(b - a)
    
