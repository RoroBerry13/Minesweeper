import random
from tkinter import messagebox

# game dimentions
width = 5
height = 5
grid = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

# generate mines
def generate_mines():
    random_x = random.randrange(0,5)
    random_y = random.randrange(0,5)

    if grid[random_x][random_y] == 0:
        grid[random_x][random_y] = '*'
    else:
        generate_mines()

for i in range(5):
    generate_mines()

# add numbers to cells
def calculate_adjacent_mines(x, y):
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

    number_of_mines = 0
    for row in temp_grid:
        for column in row:
            if column == '*':
                number_of_mines += 1

    return number_of_mines

def add_numbers():
    for x in range(height):
        for y in range(width):
            if grid[x][y] == '*':
                continue
            else:
                number_of_mines = calculate_adjacent_mines(x, y)
                grid[x][y] = number_of_mines

add_numbers()

def game_over():
    messagebox.askokcancel(title='Game Over!', message='You lost! would you like to play again?')