import matplotlib.pyplot as plt
import numpy as np
import time
from math import *
from matplotlib.pyplot import MultipleLocator

plt.ion() #开启interactive mode 成功的关键函数
plt.figure(1)
t = [0]
t_now = 0
m = [sin(t_now)]
r = [cos(t_now)]

#把y轴的刻度范围设置



for i in range(2000):
    plt.clf() 
    t_now = i * 0.1
    t.append(t_now)#模拟数据增量流入，保存历史数据
    m.append(sin(t_now))#模拟数据增量流入，保存历史数据
    r.append(cos(t_now))#模拟数据增量流入，保存历史数据= 
    if i >= 100 and i <= 1500 :
        t.pop(0)
        m.pop(0)
        r.pop(0)
    plt.plot(t,m,'-r')
    plt.plot(t,r,'-b')
    y_major_locator=MultipleLocator(10)
    ax=plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)    
    plt.ylim(-5,110)
#把y轴的主刻度设置为10的倍数
#把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白

    plt.pause(0.01)#注意此函数需要调用

