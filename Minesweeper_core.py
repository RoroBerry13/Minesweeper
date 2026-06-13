import tkinter as tk
import random

class GridBlueprint():
    def __init__(self, row= 5, column= 5, mines= 5):
        self.rows = row
        self.columns = column
        self.blueprint = []
        self.mines = mines

        self.create_empty_grid()

    def create_empty_grid(self):
        '''This function creates an empty grid'''
        self.blueprint = []
        for row in range(self.rows):
            new_row = []
            for column in range(self.columns):
                new_row.append(0)
            self.blueprint.append(new_row)

    def generate_grid(self, button_x, button_y):
        '''This function generates the grid's values after a cell is pressed'''
        for i in range(self.mines):
            self.__generate_mine(button_x, button_y)
        self.__add_numbers()

    def __generate_mine(self, button_x, button_y):
        '''This function creates a mine in a random coordinate'''
        random_x = random.randrange(0, self.rows)
        random_y = random.randrange(0, self.columns)

        # prevent a mine from generatnig in a 3x3 grid from the clicked button
        temp_grid = [
            [(button_x - 1, button_y - 1), (button_x - 1, button_y), (button_x - 1, button_y + 1)],
            [(button_x, button_y - 1), (button_x, button_y), (button_x, button_y + 1)],
            [(button_x + 1, button_y - 1), (button_x + 1, button_y), (button_x + 1, button_y + 1)]
        ]

        def check_temp_grid(temp_grid, random_x, random_y):
            for row in temp_grid:
                for tuple in row:
                    if tuple == (random_x, random_y):
                        return True
            return False

        if self.blueprint[random_x][random_y] == 0 and not check_temp_grid(temp_grid, random_x, random_y): # if the coords are not within the temporary grid, generate the mine
            self.blueprint[random_x][random_y] = '*'
        else: # if the coords of the mine are in the temporary grid or the cell != 0, generate a new coordinate
            self.__generate_mine(button_x, button_y)

 

    def __calculate_adjacent_mines(self, x, y):
        '''This function calculates the number of adjacent mines of each cell in a 3x3 grid'''
        # 3x3 grid of adjacent mines
        temp_grid = create_temp_grid(x, y, self.blueprint)

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
        '''This function creates value-less button objects'''
        for x in range(blueprint.rows):
            new_row = []
            for y in range(blueprint.columns):
                cell = Cell(master=self.frame, x_index=x, y_index=y, width=10, height=5, bg="blue")
                new_row.append(cell)
            game_grid.grid_cells.append(new_row)

    def check_grid(self):
        '''This function checks if no cell is clicked in the grid'''
        for row in self.grid_cells:
            for cell in row:
                if cell.is_visible:
                    return False
        return True
    
    def add_value_to_buttons(self):
        '''This function adds values to the button objects after the grid is created'''
        for x in range(blueprint.rows):
            for y in range(blueprint.columns):
                button = self.grid_cells[x][y]
                button.value = blueprint.blueprint[x][y]
                if blueprint.blueprint[x][y] == '*':
                    button.is_mine = True
    
    def destroy_grid(self):
        '''This function deletes the button objects'''
        self.grid_cells = []
        for widget in self.frame.winfo_children():
            widget.destroy()

    def check_game_won(self):
        '''This function checks if all the non-mine buttons are clicked'''
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

        self.bind('<Button-3>', self.flag_cell)

    def clear_adjacent_zeros(self):
        '''This function checks all the cells in a 3x3 area to clear any adjacent zeros'''
        self.is_visible = True
        # create temp 3x3 grid of adjacent cells
        temp_grid = create_temp_grid(self.x_index, self.y_index, game_grid.grid_cells)

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
        '''This function enables the flagging of potential mine cells'''
        if not self.is_visible:
            if not self.is_flagged:
                self.config(bg="yellow", state="disabled")
                self.is_flagged = True
            else:
                self.config(bg="blue", state="normal")
                self.is_flagged = False

def create_temp_grid(x, y, array):
    cell = array[x][y]
    temp_grid = [
            ['', '', ''],
            ['',cell , ''],
            ['', '', '']
        ]

        # check x index
    if not x - 1 < 0:
        temp_grid[0][1] = array[x-1][y]
        if not y - 1 < 0:
            temp_grid[0][0] = array[x-1][y-1]
        if not y + 1 > blueprint.columns - 1:
            temp_grid[0][2] = array[x-1][y+1]

    if not x + 1 > blueprint.rows - 1:
        temp_grid[2][1] = array[x+1][y]
        if not y - 1 < 0:
            temp_grid[2][0] = array[x+1][y-1]
        if not y + 1 > blueprint.columns - 1:
            temp_grid[2][2] = array[x+1][y+1]

    # check y index
    if not y - 1 < 0:
        temp_grid[1][0] = array[x][y-1]
    if not y + 1 > blueprint.columns - 1:
        temp_grid[1][2] = array[x][y+1]

    return temp_grid
    
blueprint = GridBlueprint(10, 10, 10)
game_grid = GameGrid()