import tkinter as tk
import random
from tkinter import messagebox

class GridBlueprint():
    def __init__(self, row= 5, column= 5, mines= 5):
        self.rows = row
        self.columns = column
        self.blueprint = [['*', 2, 0, 0, 0, 0, 0, 0, 0, 0], ['*', 2, 0, 0, 0, 0, 0, 0, 0, 0], [2, 2, 1, 0, 0, 0, 0, 1, 1, 1], [1, '*', 2, 1, 1, 0, 0, 1, '*', 1], [1, 1, 2, '*', 1, 0, 0, 2, 2, 2], [0, 0, 2, 2, 2, 0, 0, 1, '*', 1], [0, 0, 1, '*', 1, 0, 0, 1, 1, 1], [1, 1, 1, 2, 2, 1, 0, 0, 0, 0], ['*', 1, 0, 1, '*', 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1, '*', 1]]
        self.mines = mines

    def create_grid(self):
        self.__create_empty_grid()
        for i in range(self.mines):
            self.__generate_mines()
        self.__add_numbers()

    def __create_empty_grid(self):
        '''This function creates an empty grid'''
        self.blueprint = []
        for row in range(self.rows):
            new_row = []
            for column in range(self.columns):
                new_row.append(0)
            self.blueprint.append(new_row)

    def __generate_mines(self):
        '''This function generates mines in the grid in random coordinates'''
        random_x = random.randrange(0, self.rows)
        random_y = random.randrange(0, self.columns)

        if self.blueprint[random_x][random_y] == 0:
            self.blueprint[random_x][random_y] = '*'
        else:
            self.__generate_mines()

    def __calculate_adjacent_mines(self, x, y):
        '''This function calculates the number of adjacent mines of each cell in a 3x3 grid'''
        # 3x3 grid of adjacent mines
        temp_grid = [
            ['', '', ''],
            ['', self.blueprint[x][y], ''],
            ['', '', '']
        ]

        # check x index
        if not x - 1 < 0:
            temp_grid[0][1] = self.blueprint[x-1][y]
            if not y - 1 < 0:
                temp_grid[0][0] = self.blueprint[x-1][y-1]
            if not y + 1 > self.columns - 1:
                temp_grid[0][2] = self.blueprint[x-1][y+1]

        if not x + 1 > self.rows - 1:
            temp_grid[2][1] = self.blueprint[x+1][y]
            if not y - 1 < 0:
                temp_grid[2][0] = self.blueprint[x+1][y-1]
            if not y + 1 > self.columns - 1:
                temp_grid[2][2] = self.blueprint[x+1][y+1]

        # check y index
        if not y - 1 < 0:
            temp_grid[1][0] = self.blueprint[x][y-1]
        if not y + 1 > self.columns - 1:
            temp_grid[1][2] = self.blueprint[x][y+1]

        number_of_mines = 0
        for row in temp_grid:
            for column in row:
                if column == '*':
                    number_of_mines += 1

        return number_of_mines

    def __add_numbers(self):
        '''This function displays the number of adjacent mines in each cell'''
        for x in range(self.rows):
            for y in range(self.columns):
                if self.blueprint[x][y] == '*':
                    continue
                else:
                    number_of_mines = self.__calculate_adjacent_mines(x, y)
                    self.blueprint[x][y] = number_of_mines

class GameGrid:
    def __init__(self, frame= None):
        self.grid_cells = []
        self.frame = frame

    def create_buttons(self):
        for x in range(blueprint.rows):
            new_row = []
            for y in range(blueprint.columns):
                cell = Cell(master=self.frame, x_index=x, y_index=y, width=10, height=5, bg="blue")
                new_row.append(cell)
            game_grid.grid_cells.append(new_row)
    
    def destroy_grid(self):
        self.grid_cells = []
        for widget in self.frame.winfo_children():
            widget.destroy()

    def check_all_buttons_clicked(self):
        for row in self.grid_cells:
            for button in row:
                if button.is_mine:
                    continue
                elif button.is_visible == False and button.is_mine == False:
                    return False
        return True

class Cell(tk.Button):
    def __init__(self, x_index, y_index, master = None, bg ='white', command = "", compound = "none", cursor = "", default = "disabled", font = "TkDefaultFont", height = 0, image = "", justify = "center", overrelief = "", state = "normal", takefocus = "", text = "", underline = -1, width = 0, wraplength = 0):
        super().__init__(master, bg=bg, command=command, compound=compound, cursor=cursor, default=default, font=font, height=height, image=image, justify=justify, overrelief=overrelief, state=state, takefocus=takefocus, text=text, underline=underline, width=width, wraplength=wraplength)
        self.x_index= x_index
        self.y_index= y_index
        self.value = blueprint.blueprint[x_index][y_index]
        self.is_visible = False
        self.is_mine = False
        self.is_flagged = False

        if self.value == '*':
            self.is_mine = True

        self.bind('<Button-3>', self.flag_cell)

    def clear_adjacent_zeros(self):
        self.is_visible = True
        # create temp 3x3 grid of adjacent cells
        temp_grid = [
            ['', '', ''],
            ['', self, ''],
            ['', '', '']
        ]

        # check x index
        if not self.x_index - 1 < 0:
            temp_grid[0][1] = game_grid.grid_cells[self.x_index-1][self.y_index]
            if not self.y_index - 1 < 0:
                temp_grid[0][0] = game_grid.grid_cells[self.x_index-1][self.y_index-1]
            if not self.y_index + 1 > blueprint.columns - 1:
                temp_grid[0][2] = game_grid.grid_cells[self.x_index-1][self.y_index+1]

        if not self.x_index + 1 > blueprint.rows - 1:
            temp_grid[2][1] = game_grid.grid_cells[self.x_index+1][self.y_index]
            if not self.y_index - 1 < 0:
                temp_grid[2][0] = game_grid.grid_cells[self.x_index+1][self.y_index-1]
            if not self.y_index + 1 > blueprint.columns - 1:
                temp_grid[2][2] = game_grid.grid_cells[self.x_index+1][self.y_index+1]

        # check y index
        if not self.y_index - 1 < 0:
            temp_grid[1][0] = game_grid.grid_cells[self.x_index][self.y_index-1]
        if not self.y_index + 1 > blueprint.columns - 1:
            temp_grid[1][2] = game_grid.grid_cells[self.x_index][self.y_index+1]

        temp_grid[1][1] == ''

        for row in temp_grid:
            for cell in row:
                if cell == temp_grid[1][1]:
                    continue
                else:
                    if not cell == '':
                        if cell.is_visible == False:
                            cell.is_visible = True
                            cell.config(state= "disabled", bg="white")
                            if cell.value == 0:
                                cell.clear_adjacent_zeros()
                            else:
                                cell.config(text=cell.value)

    def flag_cell(self, event):
        if not self.is_visible:
            if not self.is_flagged:
                self.config(bg="yellow", state="disabled")
                self.is_flagged = True
            else:
                self.config(bg="blue", state="normal")
                self.is_flagged = False
    
blueprint = GridBlueprint(10, 10, 10)
print(blueprint.blueprint)
game_grid = GameGrid()