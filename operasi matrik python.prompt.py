# operasi matrik membuat 2x2

matrik = [[5,2],
        [20,2]]

def_mat = [[0 for j in range (2)] for i in range (2)]

for i in range(len(matrik)):
    for j in range(len(matrik[0])):
        def_mat[i][j] = matrik[i][j]*2

print(matrik)