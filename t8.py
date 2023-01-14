#圖表
import matplotlib.pyplot as plt
import numpy as np

#x = np.linspace(0, 10, 100)   # 產生 0～10 總共 100 連續數字
#y = 4 + 2 * np.sin(2 * x)     # 使用 NumPy 的廣播方式，產生 sin 數值的陣列 y
x = [[1,2,3,4,5],[1,2,3,4,5]]
y = [[1,2,4,8,16],[1,2,3,4,5]]
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)  # 繪製折線圖

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),  # 設定座標軸
      ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()    # 顯示圖表