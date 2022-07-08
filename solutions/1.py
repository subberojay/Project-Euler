
#adds all multiples of 3 less than x, then all multiples of 5 less than x,
#then subtracts the multiples of 15 less than x to remove the multiples of 3
#counted for a second time when summing the multiples of 5

def pe1(x):
    total = 0  
    
    for n in range(3, x, 3):
        total += n
        
    for n in range(5, x, 5):
        total += n
        
    for n in range(15, x, 15):
        total -= n
        
    return total

print(pe1(1000))
    

    