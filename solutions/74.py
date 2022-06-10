
from math import factorial

seen = {169 : 3, 363601 : 3, 1454 : 3, 871 : 2, 45361 : 2, 872 : 2, 45362 : 2}

for n in range(2, 1000000):
    n_seq = [n]
    while (sum([factorial(int(d)) for d in str(n_seq[-1])]) not in n_seq and
      sum([factorial(int(d)) for d in str(n_seq[-1])]) not in seen):
        n_seq.append(sum([factorial(int(d)) for d in str(n_seq[-1])]))
    x = sum([factorial(int(d)) for d in str(n_seq[-1])])
    if x not in seen:
        for i in range(len(n_seq)):
            seen[n_seq[i]] = len(n_seq) - i
    else:
        for i in range(len(n_seq)):
            seen[n_seq[i]] = len(n_seq) - i + seen[x]
    
print(sum(count == 60 for count in seen.values()))   