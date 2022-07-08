
#The idea is to construct decreasing palindromes from three digit numbers. 999
#gives 999999, 998 gives 998899 and so on. The largest product of two three
#digit numbers is 999*999 = 998001, so we can start from 997, which gives us
#997799, the largest palindrome less than 999*999. Next we divide the
#palindrome (m) by 1000 and add 1, as any numbers below this will need to be 
#multiplied by (at least) a four digit number to equal m. Starting from this
#number we check each potential factor to see if it divides m. As soon as we
#find one that divides m we have found a palindrome that is the product of two
#three digit numbers and we can return m.


def pe4(x):
    for n in range(10**x - 3, 1, -1):
        s = str(n)
        m = int(s + s[::-1])
        for f in range((m // 10**x) + 1, 10**x):
            if m % f == 0:
                return m