
from math import floor

squares = []
n = 0
while n**2 < 10**8:
    squares.append(n**2)
    n += 1
    
palindromes1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
palindromes_i = palindromes1

for i in range(3):
    palindromes_new = []
    for s in palindromes_i:
        for d in range(10):
            palindromes_new.append(str(d) + s + str(d))
    palindromes1 += palindromes_new
    palindromes_i = palindromes_new
    
palindromes2 = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']
palindromes_i = palindromes2

for i in range(3):
    palindromes_new = []
    for s in palindromes_i:
        for d in range(10):
            palindromes_new.append(str(d) + s + str(d))
    palindromes2 += palindromes_new
    palindromes_i = palindromes_new

palindromes = palindromes1 + palindromes2

palindromes = [p for p in palindromes if p[0] != '0'][1:]

total = 0

# squareSummable = {}

for p in palindromes:
    m = int(p)
    low, high = floor((m / 2)**0.5), floor((m / 2)**0.5) + 1
    while sum(squares[low:high + 1]) != m and low != 0:
        if sum(squares[low:high + 1]) < m:
            low -= 1
        else:
            high -= 1
    if sum(squares[low:high + 1]) == m:
        total += m
        # squareSummable[m] = (low, high)
        
print(total)