
#人员月均收支比例数据

import pandas as pd
import matplotlib.pyplot as plt
# import mpl_toolkits.axisartist.axislines as axislines

csv_data = pd.read_csv('广州呼出成本收入计算.csv',encoding="gb2312")  # 读取训练数据
# print(csv_data.shape)  #(2121, 16)

data = csv_data.iloc[:,1:]  #剪切第一列数据
# print(data.shape)     #(2121, 15)
print(data.iloc[:5,])
summary = data.describe()
# print(summary)

#时间-成本-人员 数据
data_user = data.iloc[:,4]  #人员
data_cb = data.iloc[:,16]  #比例


new_data = pd.concat([data_user,data_cb],axis=1,ignore_index=False)
print('***'*20)
print(new_data)
len = len(new_data)
print('***'*20)
print(len)



new_data2 = new_data.groupby('emp_no').mean()
# print(new_data2.shape)
len2 = new_data2.shape[0]
print('***'*20)
# print(len2)  #104
x = list(range(104))
x2 = list(range(0,104,2))



new_data_date = new_data2.index
new_data_sum_sr = new_data2['bl']
print('***'*20)
print(new_data_sum_sr)


# plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
# plt.figure(figsize=(80,4))


fig = plt.figure(1, figsize=(200,4))



plt.plot(x, new_data_sum_sr)

plt.xticks(x2, x2, rotation=0)
plt.grid()

plt.show()
# print('***'*20)
# print(new_data_sum_sr[80])