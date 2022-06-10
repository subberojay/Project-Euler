
def name_scores(filename):
    import os
    os.chdir('C:\\Users\\Punge Bilch\\Documents\\Project Euler\\files')
    f = open(filename,'r')
    names = (f.read()).split(',')
    for i in range(len(names)):
        names[i] = names[i].strip('"')
    names.sort()
    filesum = 0
    for j in range(len(names)):
        namesum = 0
        for c in names[j]:
            namesum += ord(c) - 64
        filesum += (j + 1) * namesum
    os.chdir('C:\\Users\\Punge Bilch')
    return filesum