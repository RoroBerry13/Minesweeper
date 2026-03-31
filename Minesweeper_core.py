import tkinter as tk

# round attributes
seconds = 0

# game settings
row = 5
column = 5

grid = []

# game logic
def cell_clicked(cell):
    cell.config(text="clicked!")