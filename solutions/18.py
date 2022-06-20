
f = open('files\p18.txt', 'r')
t = (f.read()).split('\n')
if t[-1] == '':
    t = t[:-1]
tri = [t[i].split() for i in range(len(t))]
prev_max = [int(tri[0][0])]
for r in range(1, len(tri)):
    new_max = [0] * (len(prev_max) + 1)
    for v in range(1, len(new_max) - 1):
        new_max[v] = max(prev_max[v - 1] + int(tri[r][v]), prev_max[v] + int(tri[r][v]))
    new_max[0] = prev_max[0] + int(tri[r][0])
    new_max[-1] = prev_max[-1] + int(tri[r][-1])
    prev_max = new_max
print(max(new_max))
    