import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title("Fucking Awesome!")

# Disable resizing the GUI
#window.resizable(width=0, height=0)

# Adding a Label
ttk.Label(window, text="Emter a name:").grid(column=0, row=0)
#aLabel = ttk.Label(window, text="A Label")
#aLabel.grid(column=0, row=0)

# Button Click Event Callback Fuction
def click_me ():
    action.configure(text="Hello {} {}!".format(name.get(), number_chosen.get()))

# Adding a Button
action = ttk.Button(window, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(window, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

ttk.Label(window, text="Choose a number:").grid(column=1, row=0)

number = tk.StringVar()
number_chosen = ttk.Combobox(window, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 3, 4, 43, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Place cursor into name Entry
name_entered.focus()

# Disable the Button Widget
#action.configure(state='disable')

# Creating three checkbuttons
ch_var_dis = tk.IntVar()
check1 = tk.Checkbutton(window, text="Disable", variable=ch_var_dis, state='disable')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

ch_var_un = tk.IntVar()
check2 = tk.Checkbutton(window, text="UnChecked", variable=ch_var_un)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

ch_var_en = tk.IntVar()
check3 = tk.Checkbutton(window, text="Enable", variable=ch_var_en)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# Radiobutton Globals
colors = ["Blue", "Gold", "Red"]

# Radiobutton callback
def rad_call ():
    rad_sel = rad_var.get()
    if   rad_sel == 0: window.configure(background=colors[0])
    elif rad_sel == 1: window.configure(background=colors[1])
    elif rad_sel == 2: window.configure(background=colors[2])

# Create three Radiobuttons
rad_var = tk.IntVar()
rad_var.set(99)

for col in range(3):
    cur_rad = 'rad' + str(col)
    cur_rad = tk.Radiobutton(window, text=colors[col], variable=rad_var, value=col, command=rad_call)
    cur_rad.grid(column=col, row=5, sticky=tk.W)

# Using a scrolled Text control
scroll_w = 30
scroll_h = 3

src = scrolledtext.ScrolledText(window, width=scroll_w, height=scroll_h, wrap=tk.WORD)
src.grid(column=0, columnspan=3)

window.mainloop()