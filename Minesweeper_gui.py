import tkinter as tk
from tkinter import ttk
import Minesweeper_core as core

window = tk.Tk()
window.geometry('500x500')

frame = tk.Frame(window, bg='red')
frame.grid(row=0, column=0, sticky='nsew')
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)

for row in range(len(core.grid)):
    for column in range(len(core.grid[row])):
        if core.grid[row][column] == '*':
            cell = tk.Button(frame, text=core.grid[row][column], command=core.game_over)
            cell.grid(row=row, column=column)
        else:
            cell = tk.Button(frame, text= core.grid[row][column])
            cell.grid(row=row, column=column)

window.mainloop()