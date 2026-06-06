import tkinter as tk
from tkinter import ttk
import Minesweeper_core as core

window = tk.Tk()
window.geometry('800x800')

frame = tk.Frame(window, bg='red')
frame.grid(row=0, column=0, sticky='nsew')
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)

for x in range(core.blueprint.rows):
    new_row = []
    for y in range(core.blueprint.columns):
        cell = core.Cell(master=frame, x_index=x, y_index=y, width=10, height=5, bg="blue")
        cell.grid(row=x, column=y)
        new_row.append(cell)
    core.grid.grid_cells.append(new_row)

window.mainloop()