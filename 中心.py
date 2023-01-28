import tkinter 

root=tkinter.Tk()
root.title('My Test Appwin in Center')

appwin_width = 1024
appwin_height = 768
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
appwinx= (screen_width-appwin_width)/2
appwiny=(screen_height-appwin_height)/2
root.geometry(f'{appwin_width}x{appwin_height}+{int(appwinx)}+{int(appwiny)}')
root.mainloop()