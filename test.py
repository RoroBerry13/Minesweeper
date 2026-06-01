height = 5
width = 5
grid = [
    [6,0,0,0,5],
    [0,2,0,4,0],
    [0,6,0,0,1],
    [7,0,9,0,0],
    [0,8,0,10,0]
]

x = 4
y = 4

# 3x3 grid of adjacent mines
temp_grid = [
    ['', '', ''],
    ['', grid[x][y], ''],
    ['', '', '']
]

# check x index
if not x - 1 < 0:
    temp_grid[0][1] = grid[x-1][y]
    if not y - 1 < 0:
        temp_grid[0][0] = grid[x-1][y-1]
    if not y + 1 > height - 1:
        temp_grid[0][2] = grid[x-1][y+1]

elif not x + 1 > height - 1:
    temp_grid[2][1] = grid[x+1][y]
    if not y - 1 < 0:
        temp_grid[2][0] = grid[x+1][y-1]
    if not y + 1 > width - 1:
        temp_grid[2][2] = grid[x+1][y+1]

# check y index
if not y - 1 < 0:
    temp_grid[1][0] = grid[x][y-1]
elif not y + 1 > width - 1:
    temp_grid[1][2] = grid[x][y+1]

print(temp_grid)