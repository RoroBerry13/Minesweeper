import tkinter as tk

class Grid():
    def __init__(self, row=5, column=5):
        self.rows = row
        self.columns = column
        self.grid = []

    def create_grid(self):
        for row in range(self.rows):
            new_row = []
            for column in range(self.columns):
                new_row.append(0)
            self.grid.append(new_row)

    def print_dimensions(self):
        print(f'this grid is {self.rows} x {self.columns}')
        print(self.grid)

new_grid = Grid()
new_grid.create_grid()
new_grid.print_dimensions()