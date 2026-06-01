import tkinter as tk
import random
from tkinter import messagebox

class Grid():
    def __init__(self, row= 5, column= 5, mines= 5):
        self.rows = row
        self.columns = column
        self.grid = []
        self.mines = mines

        self.create_grid()
        for i in range(mines):
            self.generate_mines()
        self.add_numbers()

    def create_grid(self):
        '''This function creates an empty grid'''
        for row in range(self.rows):
            new_row = []
            for column in range(self.columns):
                new_row.append(0)
            self.grid.append(new_row)

    def print_dimensions(self):
        print(self.grid)

    def generate_mines(self):
        '''This function generates mines in the grid in random coordinates'''
        random_x = random.randrange(0, self.rows)
        random_y = random.randrange(0, self.columns)

        if self.grid[random_x][random_y] == 0:
            self.grid[random_x][random_y] = '*'
        else:
            self.generate_mines()

    def calculate_adjacent_mines(self, x, y):
        '''This function calculates the number of adjacent mines of each cell in a 3x3 grid'''
        # 3x3 grid of adjacent mines
        temp_grid = [
            ['', '', ''],
            ['', self.grid[x][y], ''],
            ['', '', '']
        ]

        # check x index
        if not x - 1 < 0:
            temp_grid[0][1] = self.grid[x-1][y]
            if not y - 1 < 0:
                temp_grid[0][0] = self.grid[x-1][y-1]
            if not y + 1 > self.columns - 1:
                temp_grid[0][2] = self.grid[x-1][y+1]

        if not x + 1 > self.rows - 1:
            temp_grid[2][1] = self.grid[x+1][y]
            if not y - 1 < 0:
                temp_grid[2][0] = self.grid[x+1][y-1]
            if not y + 1 > self.columns - 1:
                temp_grid[2][2] = self.grid[x+1][y+1]

        # check y index
        if not y - 1 < 0:
            temp_grid[1][0] = self.grid[x][y-1]
        if not y + 1 > self.columns - 1:
            temp_grid[1][2] = self.grid[x][y+1]

        number_of_mines = 0
        for row in temp_grid:
            for column in row:
                if column == '*':
                    number_of_mines += 1

        return number_of_mines

    def add_numbers(self):
        '''This function displays the number of adjacent mines in each cell'''
        for x in range(self.rows):
            for y in range(self.columns):
                if self.grid[x][y] == '*':
                    continue
                else:
                    number_of_mines = self.calculate_adjacent_mines(x, y)
                    self.grid[x][y] = number_of_mines

grid = Grid(10, 10, 20)

def game_over():
    retry = messagebox.askokcancel(title='Game Over!', message='You lost! would you like to play again?')