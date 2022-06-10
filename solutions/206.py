
import numpy as np

n = int(np.ceil(np.sqrt(1020304050607080900)))

while str(n)[-2:] != '70':
    n += 1

while True:
    s = str(n**2)
    if (s[0] == '1' and s[2] == '2' and s[4] == '3' and s[6] == '4' and s[8] == '5' and
        s[10] == '6' and s[12] == '7' and s[14] == '8' and s[16] == '9' and s[17] == '0'):
        break
    n += 100
    
print(n)
        

        