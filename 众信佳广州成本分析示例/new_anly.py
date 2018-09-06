#时间-收入-成本 全量数据


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
data_date = data.iloc[:,2]  #时间
data_sr = data.iloc[:,3]  #收入
data_cb = data.iloc[:,15]  #成本


def mkline(x_line,y_line,label):
    new_data = pd.concat([x_line,y_line],axis=1,ignore_index=False)
    print('***'*20)
    print(new_data)
    len1 = len(new_data)
    print('***'*20)
    print(len1)



    new_data2 = new_data.groupby('date').sum()
    # print(new_data2.shape)
    len2 = new_data2.shape[0]
    print('***'*20)
    # print(len2)  #104
    x = list(range(32))
    x2 = list(range(32))




    new_data_date = new_data2.index
    new_data_sum_sr = new_data2[label]
    print('***'*20)
    print(new_data_sum_sr)


    # plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
    # plt.figure(figsize=(80,4))


    fig = plt.figure(1, figsize=(200,4))



    return plt.plot(new_data_sum_sr.index, new_data_sum_sr)


mkline(data_date,data_sr,label='sum_sr')
mkline(data_date,data_cb,label='sum_cb')

x2 = list(range(32))
plt.xticks(x2, x2, rotation=0)
plt.grid()

plt.show()
# print('***'*20)
# print(new_data_sum_sr[80])