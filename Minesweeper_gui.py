import tkinter as tk
from tkinter import messagebox
import Minesweeper_core as core

window = tk.Tk()
window.geometry('800x875')

menu = tk.Menu(window)
window.config(menu=menu)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

def new_game():
    core.blueprint.create_empty_grid()
    core.game_grid.destroy_grid()
    grid_buttons()

file_menu.add_command(label="Create_new_game", command=lambda:new_game())
file_menu.add_command(label="Exit", command=window.quit)

grid_frame = tk.Frame(window, bg='red')
grid_frame.grid(row=0, column=0, sticky='nsew')

core.game_grid.frame = grid_frame
def grid_buttons():
    core.game_grid.create_buttons()
    for row in core.game_grid.grid_cells:
        for button in row:
            button.config(command=lambda button=button: button_clicked(button))
            button.grid(row= button.x_index, column= button.y_index)

grid_buttons()

def button_clicked(button):
    if core.game_grid.check_grid():
        core.blueprint.generate_grid(button.x_index, button.y_index)
        core.game_grid.add_value_to_buttons()
    button.config(state="disabled", bg= "white")
    button.is_visible = True
    if button.is_mine:
        button.config(bg="red")
        disable_all_buttons()
        retry = messagebox.askokcancel("Game Over", "You Lost! Would you like to play again?")
        if retry:
            new_game()
    elif button.value == 0:
        button.clear_adjacent_zeros()
    else:
        button.config(bg="white", text=button.value)
    game_won = core.game_grid.check_game_won()
    if game_won:
        disable_all_buttons()
        play_again = messagebox.askokcancel("You won!", "Play again?")
        if play_again:
            new_game()

def disable_all_buttons():
    for row in core.game_grid.grid_cells:
        for button in row:
            button.config(state="disabled")
            button.unbind('<Button-3>')

window.mainloop()