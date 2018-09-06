# -*- coding:utf-8 -*-

import xlrd
import pymysql
import math
import ctype
import os
import logging
import datetime
from xlrd import xldate_as_tuple

__author__ = 'jdf'

logger = logging.getLogger('logger')

#执行语句
def execute_sql(sql):
    # conn = pymysql.connect(self.host, self.port, self.user, self.password, self.db)
    conn = pymysql.connect(host='localhost', port=3306, user='jdf', passwd='12345', db='pymysql_db')
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except pymysql.Error as e:
        logger.error('Error code: %s, message: %s, sql: %s' % (e.args[0], e.args[1], sql))

    conn.commit()

    cur.close()
    conn.close()



# 读取文件内容，默认跳过表头，默认第一个sheet
def read_excel(path, tip=0, index=0):
    book = xlrd.open_workbook(path)
    # sheet = book.sheet_by_name('gztx_gz_07')
    sheet = book.sheet_by_index(index)
    value = []
    type = []
    for r in range(tip, sheet.nrows):
        ops1 = []
        ops2 = []
        for i in range(sheet.ncols):
            values = sheet.cell(r, i)
            if values.ctype == 3:
                date = xldate_as_tuple(values.value,0)
                values.value = datetime.datetime(*date)
            ops1.append(values.value)  # value
            ops2.append(values.ctype)  # type
        value.append(ops1)
        type.append(ops2)
    return value, type

# value, type = read_excel(new_path, 0)

# 生成建表sql
def create_table_sql(table_name, value, type):

    field = value[0]
    field_type = type[1]
    # print(field)
    # print(value[1])
    # print(field_type)

    sql_start = 'CREATE TABLE %s (' %table_name
    sql_cut = ''

    for i in range(len(field)):
        # print(i)
        if field_type[i] == 2:
            sql_cut = '%s VARCHAR(1000),' % field[i]  #DECIMAL(10,2)
        # elif field_type[i] == 3:
        #     sql_cut = '%s datetime,' % field[i]
        else:
            sql_cut = '%s VARCHAR(1000),' % field[i]
        sql_start += sql_cut

    # print(sql)
    sql_end = ');'
    sql_finally = sql_start[:-1] + sql_end
    # print(sql_finally)
    return sql_finally


#生成插入语句sql
def insert_exc_sql(table_name, value):
    sql_end = ''
    conn = pymysql.connect(host='localhost', port=3306, user='jdf', passwd='12345', db='pymysql_db')
    cur = conn.cursor()
    num = 0
    for n in range(1, len(value)):
        # sql = 'insert into joke (gid,name)value(0,"joker");'

        # 插入sql语句前半部分
        sql_start = 'insert into %s (' % table_name

        # 插入sql语句字段名部分
        field = value[0]
        field_sql = ''
        for i in field:
            if isinstance(i, str) == True:
                sql = i + ','
            else:
                sql = str(i) + ','
            field_sql += sql
        sql_mid = sql_start + field_sql[:-1] + ') value ('

        # 插入sql语句字段值部分
        values = value[n]
        values_sql = ''
        for i in values:
            if isinstance(i, int) == True:
                sql = str(i) + ','
            elif isinstance(i, float) == True:
                sql = str(i) + ','
            else:
                sql = '"' + str(i) + '",'
            values_sql += sql


        sql_end = sql_mid + values_sql[:-1] + ');'



        try:
            cur.execute(sql_end)
            num += 1
        except pymysql.Error as e:
            logger.error('Error code: %s, message: %s, sql: %s' % (e.args[0], e.args[1], sql_end))

    conn.commit()
    print("导入%d条数据" %num)

    cur.close()
    conn.close()


if __name__ == "__main__":

    # star_time = datetime.datetime.now()
    # # excel = Exceltomysql(host='127.0.0.1', user='jdf', password='12345', path='/Users/yh/Desktop/分析测试文件/gztx_gz_07.xls', table_name='gztx_gz_01')
    # path = '/Users/yh/Desktop/分析测试文件/gztx_gz_07.xls'
    # table_name = 'gztx_gz_07'
    #
    #
    # value, type = read_excel(path)
    # create_table_sql = create_table_sql(table_name, value, type)
    # print('生成表语句：  ' + create_table_sql)
    # print('---'*20)
    # execute_sql(create_table_sql)
    # print('生成表%s' %table_name)
    # print('---' * 20)
    #
    # insert_exc_sql(table_name,value)
    #
    # end_time = datetime.datetime.now()
    # time = end_time - star_time
    # print('消耗时间' + str(time))
    pass