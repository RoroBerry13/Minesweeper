import tkinter as tk
from tkinter import messagebox
import Minesweeper_core as core

run_game = True

window = tk.Tk()
window.geometry('800x800')

menu = tk.Menu(window)
window.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

def new_game():
    core.blueprint.create_grid()
    core.game_grid.destroy_grid()
    grid_buttons()
    apply_command_to_buttons()

file_menu.add_command(label="Create_new_game", command=lambda:new_game())
file_menu.add_command(label="Exit", command=window.quit)

grid_frame = tk.Frame(window, bg='red')
grid_frame.grid(row=0, column=0, sticky='nsew')
grid_frame.rowconfigure(0, weight=1)
grid_frame.columnconfigure(0, weight=1)

core.game_grid.frame = grid_frame
def grid_buttons():
    core.game_grid.create_buttons()
    for row in core.game_grid.grid_cells:
        for button in row:
            button.grid(row= button.x_index, column= button.y_index)

grid_buttons()

def button_clicked(button):
    button.config(state="disabled", bg= "white")
    if button.is_mine:
        button.config(bg="red")
        retry = messagebox.askokcancel("Game Over", "You Lost! Would you like to play again?")
        if retry:
            new_game()
    elif button.value == 0:
        button.clear_adjacent_zeros()
    else:
        button.config(bg="white", text=button.value)

def apply_command_to_buttons():
    for row in core.game_grid.grid_cells:
        for button in row:
            button.config(command=lambda button=button: button_clicked(button))

apply_command_to_buttons()

window.mainloop()