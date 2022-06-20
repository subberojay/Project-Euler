
filename = 'files//p081_matrix.txt'



with open(filename, 'r') as f:
    matrix = (f.read()).split('\n')
 
matrix = matrix[:-1]
for i in range(len(matrix)):
    matrix[i] = matrix[i].split(',')

for j in range(1, len(matrix)):
    matrix[0][j] = int(matrix[0][j]) + int(matrix[0][j - 1])

for i in range(1, len(matrix)):
    matrix[i][0] = int(matrix[i][0]) + int(matrix[i - 1][0])
    for j in range(1, len(matrix)):
        s = int(min(matrix[i - 1][j], matrix[i][j - 1]))
        matrix[i][j] = int(matrix[i][j]) + s
        
print(matrix[-1][-1])
 