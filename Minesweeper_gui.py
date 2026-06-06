import tkinter as tk
from tkinter import ttk
import Minesweeper_core as core

window = tk.Tk()
window.geometry('800x800')

frame = tk.Frame(window, bg='red')
frame.grid(row=0, column=0, sticky='nsew')
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)

for x in range(core.grid.rows):
    for y in range(core.grid.columns):
        if core.grid.grid[x][y] == '*':
            cell = core.Cell(master=frame, x_index=x, y_index=y, value=core.grid.grid[x][y], width= 10, height=5, is_mine=True)
            cell.grid(row=x, column=y)
        else:
            cell = core.Cell(master=frame, x_index=x, y_index=y, value=core.grid.grid[x][y], width=10, height=5)
            cell.grid(row=x, column=y)

window.mainloop()