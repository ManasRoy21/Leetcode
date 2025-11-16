input_matrix = [[1,1,1],[1,0,1],[1,1,1]]

rows = set()
cols = set()

for i in range(len(input_matrix)):
    for j in range(len(input_matrix[i])):
        if input_matrix[i][j] == 0:
            rows.add(i)
            cols.add(j)


for r in rows:
    input_matrix[r] = [0] * len(input_matrix[r])

for c in cols:
    for i in range(len(input_matrix)):
        input_matrix[i][c] = 0

print(input_matrix) 