#子視窗
import tkinter as tk

def createNewWindow():
    newWindow = tk.Toplevel(app)
    newWindow.wm_attributes('-topmost',1)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()

app = tk.Tk()
app.wm_attributes('-topmost',1)
buttonExample = tk.Button(app, 
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()

app.mainloop()