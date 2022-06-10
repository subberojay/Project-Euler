
import itertools

pandigitals = [x for x in itertools.permutations(list(range(10)))]
              
pan_sum = 0

for p in pandigitals:
    if p[3] % 2 == 0 and p[5] % 5 == 0:
        m = ''
        for digit in p:
            m += str(digit)
        if int(m[1:4]) % 2 == 0 and int(m[2:5]) % 3 == 0 and int(m[3:6]) % 5 == 0 and int(m[4:7]) % 7 == 0 and int(m[5:8]) % 11 == 0 and int(m[6:9]) % 13 == 0 and int(m[7:]) % 17 == 0:
            pan_sum += int(m)

print(pan_sum)