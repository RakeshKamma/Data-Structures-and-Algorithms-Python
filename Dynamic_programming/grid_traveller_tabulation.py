# m - rows
# n - columns

def grid_tab(m,n):
    table= [[0 for _ in range(n+1)] for _ in range(m+1)]
    table[1][1]=1
    for i in range(m+1):
        for j in range(n+1):
            if i+1<m+1:
                table[i+1][j]+=table[i][j]
            if j+1<n+1:
                table[i][j+1]+=table[i][j]

    return table[m][n]

print(grid_tab(1,1))
print(grid_tab(2,3))
print(grid_tab(3,2))
print(grid_tab(3,3))
print(grid_tab(18,18))



