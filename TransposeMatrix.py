Matrix = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(Matrix)):
   # iterate through columns
   for j in range(len(Matrix[0])):
       result[j][i] = Matrix[i][j]

for r in result:
   print(r)