import xlrd
import pymysql
import math
import ctype
import os

new_path = '/Users/yh/Desktop/分析测试文件/gztx_gz_07.xls'


#读取文件内容，默认跳过表头，默认第一个sheet
def read_excel(path,tip=1,index=0):
    book = xlrd.open_workbook(path)
    # sheet = book.sheet_by_name('gztx_gz_07')
    sheet = book.sheet_by_index(index)
    value = []
    type = []
    for r in range(tip, sheet.nrows):
        ops1 = []
        ops2 =[]
        for i in range(sheet.ncols):
            values = sheet.cell(r, i)
            ops1.append(values.value)  #value
            ops2.append(values.ctype)  #type
        value.append(ops1)
        type.append(ops2)
    return value, type

value, type = read_excel(new_path,0)
print(value[1:])
# print(type[1])
print('***'*20)


#生成建表sql
# def create_table_sql(table_name):
#
#     field = value[0]
#     field_type = type[1]
#     print(field)
#     print(value[1])
#     print(field_type)
#
#     sql_start = 'CREATE TABLE %s (' %table_name
#     sql_cut = ''
#
#     for i in range(len(field)):
#         # print(i)
#         if field_type[i] == 2:
#             sql_cut = '%s DECIMAL(10,2),' % field[i]
#         elif field_type[i] == 3:
#             sql_cut = '%s date,' % field[i]
#         else:
#             sql_cut = '%s VARCHAR(1000),' % field[i]
#         sql_start += sql_cut
#
#     # print(sql)
#     sql_end = ');'
#     sql_finally = sql_start[:-1] + sql_end
#     # print(sql_finally)
#     return sql_finally
#
# create_sql = create_table_sql('hudah')
# print(sql)


#执行sql
# def execute_sql(sql):
#     conn = pymysql.connect(host='localhost', port=3306, user='jdf', passwd='12345', db='pymysql_db')
#     cur = conn.cursor()
#     cur.execute(sql)
#     conn.commit()
#     cur.close()
#     conn.close()
#


#插入sql语句生成
def insert_sql(table_name, value):
    sql_ending = ''
    for n in range(1, len(value)):
        # sql = 'insert into joke (gid,name)value(0,"joker");'

        #插入sql语句前半部分
        sql_start = 'insert into %s (' %table_name

        #插入sql语句字段名部分
        field = value[0]
        field_sql = ''
        for i in field:
            if isinstance(i, str) == True:
                sql = i + ','
            else:
                sql = str(i) + ','
            field_sql += sql
        sql_mid = sql_start + field_sql[:-1] +') value ('

        # 插入sql语句字段值部分
        values = value[n]
        values_sql = ''
        for i in values:
            if isinstance(i, str) == True:
                sql = '"' + i + '",'
            else:
                sql = str(i) + ','
            values_sql += sql

        # print(values_sql)

        sql_end = sql_mid + values_sql[:-1] + ');'
        sql_ending += sql_end
    print(sql_ending)
    return sql_ending



insert_sql('hudah',value)


















# filelist = ['activity_password1.xlsx', 'activity_password2.xlsx', 'activity_password3.xlsx', \
#             'activity_password4.xlsx', 'activity_password5.xlsx', 'activity_password6.xlsx', \
#             'activity_password6_1.xlsx', 'activity_password7.xlsx', 'activity_password8.xlsx']

# filelist = ['/Users/yh/Desktop/分析测试文件/gztx_gz_07.xls']
#
# for i in range(1, 100):
#     # 建立mysql连接
#     conn = pymysql.connect(
#             host = '127.0.0.1',
#             user='root',
#             passwd = '12345',
#             db='pymysql_db', #+ str(i),
#             port=3306,
#             charset='utf8'
#         )
#
#     # 获得游标
#     cur = conn.cursor()
#
#     for filename in filelist:
#         book = xlrd.open_workbook(filename)
#         sheet = book.sheet_by_name('@gztx_gz_07')
#         ops = []
#         for r in range(1, sheet.nrows):
#             values = (sheet.cell(r, 0).value, sheet.cell(r, 1).value, sheet.cell(r, 2).value, sheet.cell(r, 3).value)
#             ops.append(values)
#         n = math.ceil(len(ops) / 5000)
#         for n1 in range(0, n):
#             cur.executemany('insert into gm_password (id, type, code, status) values (%s, %s, %s, %s)', ops[5000*n1:5000*(n1+1)])
#     cur.close()
#     conn.commit()
#     conn.close()
#     print ('youxi'+str(i)+' sucess')