import os

os.chdir('C:\\Users\\Punge Bilch\\Documents\\Project Euler\\files')

with open('p102_triangles.txt') as triangles:
    count = 0
    for rows in triangles:
        coords = rows.split(',')
        p = [int(x) for x in coords]
        crossProds = [p[1]*(p[0] - p[4]) - p[0]*(p[1] - p[5]),
                      p[3]*(p[2] - p[0]) - p[2]*(p[3] - p[1]),
                      p[5]*(p[4] - p[2]) - p[4]*(p[5] - p[3])]
        if not min(crossProds) < 0 < max(crossProds):
            count += 1
    print(count)