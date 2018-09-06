#时间-收入-人员 数据


import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('广州呼出成本收入计算.csv',encoding="gb2312")  # 读取训练数据
# print(csv_data.shape)  #(2121, 16)

data = csv_data.iloc[:,1:]  #剪切第一列数据
# print(data.shape)     #(2121, 15)
print(data.iloc[:5,])
summary = data.describe()
# print(summary)

#时间-成本-人员 数据
data_date = data.iloc[:,2] #时间
data_cb = data.iloc[:,3]  #s收入
data_user = data.iloc[:,5]  #人员

new_data = pd.concat([data_date,data_cb,data_user],axis=1,ignore_index=False)
print(new_data)
len = len(new_data)


new_data1 = new_data[:]
# print(new_data1)

#剪切时间格式多余的数字

# for i in range(31):
#     s = '2018-07-%02d 00:00:00' % i
#     new_data2 = new_data1.replace(s,i)
#     print(new_data2)


# print(new_data2)


n = 0
for i,j in new_data1.groupby('emp_name'):
    # print('*'*13+i+'*'*13+'\n',j)


    j = j.sort_values(by='date')    #组内排序
    print(j)
    date1 = j['date']
    # print(date1)
    cb1 = j['sum_sr']
    # print(cb1)
    plt.plot(date1, cb1)
    # print(i)
    n += 1
    # if n < 5:
    #     plt.show()
plt.xticks(list(range(32)), list(range(32)), rotation=0)


plt.show()










# x = new_data[0][:]
# print(str(x[0])[8:10])
# import matplotlib.pyplot as plt
# # 1.线图
# #调用plt。plot来画图,横轴纵轴两个参数即可
# plt.plot(data_date,data_cb)
# # python要用show展现出来图
# plt.show()