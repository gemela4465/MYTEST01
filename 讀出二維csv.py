import pandas as pd
df = pd.read_csv('iris.csv',header = None)#因为没有表头，不把第一行作为每一列的索引
data = []
for i in df.index:
  data.append(tuple(df.values[i]))
allnodes = tuple(data)#若想用二维列表的形式读取即删掉此行语句
print(allnodes[1][0])
