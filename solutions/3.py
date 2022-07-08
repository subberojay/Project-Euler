
#divides out each prime factor one by one, starting from 2 and increasing.
#Once n = 1 we have divided out the last prime factor and as we are 
#increasing as we go this must be the greatest.

def pe3(x):
    pf = 2
    while x != 1:
        while x % pf == 0:
            x //= pf
        pf += 1
    return(pf - 1)