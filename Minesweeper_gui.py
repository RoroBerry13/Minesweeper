import tkinter as tk
from tkinter import ttk
import Minesweeper_core as core

# window attributes
window = tk.Tk()
window.geometry('500x500')
# window.state("zoomed") #DISABLED TEMPORARILY
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1) # allow window to expand when zoomed


# window layout
frm = tk.Frame(window, bg="red")
frm.grid(row=0, column=0, sticky="nsew")
frm.rowconfigure(1, weight=1)
frm.columnconfigure(1, weight=1)


# title
tk.Label(frm, text="MineSweeper", font=(27)).grid(row=0, column=1, sticky="ew", padx=10, pady=10)


# game buttons
game_grid = tk.Frame(frm, bg="blue")
game_grid.grid(row=1, column=1, sticky="nsew")
game_grid.rowconfigure(0, weight=1)
game_grid.columnconfigure(0, weight=1)

buttons = tk.Frame(game_grid)
buttons.grid()
for cell_x in range(core.row):
    for cell_y in range(core.column):
        tk.Button(buttons, text=f"({cell_x}, {cell_y})").grid(row=cell_x, column=cell_y)


# timer
timer_frame = tk.Frame(frm, bg="yellow")
timer_frame.grid(row=2, column=0, padx=50, pady=50)

timer = tk.Label(timer_frame, text=f"00:00")
timer.grid()

def increase_timer():
    core.seconds += 1

    mins = core.seconds // 60
    secs = core.seconds % 60

    label_time = f"{mins:02}:{secs:02}"

    timer.config(text=label_time)
    window.after(1000, increase_timer)

increase_timer()



window.mainloop()
