#動態圖表

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from tkinter import *


def video_loop():  #動態圖像現實窗口
    """
    動態matlib圖表
    """
    rand_data = abs(np.random.normal(1, 2, 12))
    f.clf()
    a = f.add_subplot(111)
    a.bar(range(12),abs(rand_data), align='center')
    a.set_title('title')
    canvas.draw()
    root.after(500, video_loop)


root = Tk()
root.title("Set title")
root.geometry('1024x800')

"""
圖像畫布設置
"""
panel = Label(root)  # initialize image panel
panel.place(x=0,y=0,anchor='nw')
root.config(cursor="arrow")
"""
右側組件
"""
l1 = Label(root,text = "可以添加更多組件",bg='green',font=('Arial', 12), width=22, height=2)
l1.place(x=342,y=0,anchor='nw')

matplotlib.use('TkAgg')
f = Figure(figsize=(3,3), dpi=120)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().place(x=200,y=300 ,anchor='nw')

video_loop()
root.mainloop()

#test