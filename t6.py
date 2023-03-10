#關窗模式
import tkinter as tk
from tkinter import messagebox

UserName = ""

class MyCollectApp(tk.Toplevel):#重点
    def __init__(self):
        super().__init__() #重点
        self.title('用户信息')
        self.setupUI()

    def setupUI(self):
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        l1 = tk.Label(row1, text="用户名：",height=2,width=10)
        l1.pack(side=tk.LEFT)  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
        self.xls_text = tk.StringVar()
        tk.Entry(row1, textvariable=self.xls_text).pack(side=tk.RIGHT)

        row2 = tk.Frame(self)
        row2.pack(fill="x")
        tk.Button(row2, text="点击确认", command=self.on_click).pack(side=tk.RIGHT)

    def on_click(self):
        #print(self.xls_text.get().lstrip())
        global UserName
        UserName = self.xls_text.get().lstrip()
        if len(UserName) == 0:
            #print("用户名必须输入!")
            messagebox.showwarning(title='系统提示',message='请输入用户名!')
            return False
        self.quit()
        self.destroy()
        print("用户名：%s" % (UserName))

if __name__ == '__main__':
    var_box = tk.messagebox.askyesno(title='系统提示', message='是否采集人脸数据需要')  # 返回'True','False'
    if var_box:
        app = MyCollectApp()
        app.mainloop()
    else:
        print('不做处理')
