import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('广州呼出成本收入计算.csv',encoding="gb2312")  # 读取训练数据
# print(csv_data.shape)  #(2121, 16)

data = csv_data.iloc[:,1:]  #剪切第一列数据
# print(data.shape)     #(2121, 15)
# print(data.iloc[:5,])
summary = data.describe()
# print(summary)

#时间-成本-人员 数据
data_date = data.iloc[:,2] #时间
data_cb = data.iloc[:,3]  #成本
data_user = data.iloc[:,5]  #人员



new_data = pd.concat([data_date,data_cb],axis=1,ignore_index=False)
# print(new_data.shape)
len = len(new_data)


# new_data1 = new_data[:500]
# print(new_data1)



n = 0
# for i,j in new_data1.groupby('date'):
#     print('*'*13+i+'*'*13+'\n',j)

new_data2 = new_data.groupby('date').sum()
# print(new_data2.shape)

new_data_date = new_data2.index
new_data_sum_sr = new_data2['sum_sr']
print(new_data_sum_sr)


plt.plot(new_data_date, new_data_sum_sr)
plt.show()
