
#Creates a list of the first x primes. Starts at 2, then checks each natural
#number n to see if any of the previously recorded primes up to root n divide n.
#If none do then n has no prime factors less than it, so must be prime.

def pe7(x):
    primes = [2]
    n = primes[-1]
    while len(primes) < x:
        nPrime = False
        while nPrime is False:
            n += 1
            nPrime = True
            cap = n**0.5
            for p in primes:
                if p > cap:
                   break
                if n % p == 0:
                    nPrime = False
                    break
        primes.append(n)
    return(n)
    
            
                
        