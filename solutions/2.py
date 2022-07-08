
#from 2 every third term in the fibonacci sequence is even. a holds the even
#term and b the preceding term, from these the next even term and preceding 
#term are generated, with a being added to the total


def pe2(x):
    b, a = 1, 2
    total = 0
    
    while a <= x:
        total += a
        a, b = 3 * a + 2 * b, 2 * a + b
        
    return total
    
print(pe2(4000000))
    
