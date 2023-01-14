#選單
import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('200x200')

def open():
    print('open')
    menubar.entryconfig('Save', state='normal')
def save(): print('save')
def exit():
    print('exit')
    menubar.entryconfig('Save', state='disabled')

menu = tk.Menu(root)
menubar = tk.Menu(menu)
menubar.add_command(label="Open", command=open, state="normal")
menubar.add_command(label="Save", command=save, state="disabled")
menubar.add_command(label="Exit", command=exit)
menu.add_cascade(label='File', menu=menubar)

root.config(menu=menu)

root.mainloop()
