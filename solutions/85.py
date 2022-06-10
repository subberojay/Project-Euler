
def rectangleCount(rows, columns):
    rectangles = 0
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            rectangles += (rows - (i - 1)) * (columns - (j - 1))
    return rectangles
    
rows, columns = 1, 1
closestPair = [(1, 1), 1999999]

while rectangleCount(rows, columns) < 2000000:
    columns += 1
    
columns -= 1
    
while rows <= columns:
    if rectangleCount(rows, columns + 1) - 2000000 < closestPair[1]:
        closestPair = [(rows, columns + 1), rectangleCount(rows, columns + 1) - 2000000]
    if 2000000 - rectangleCount(rows, columns) < closestPair[1]:
        closestPair = [(rows, columns), 2000000 - rectangleCount(rows, columns)]
    rows += 1
    while rectangleCount(rows, columns) > 2000000:
        columns -= 1
        
print(closestPair[0][0] * closestPair[0][1])