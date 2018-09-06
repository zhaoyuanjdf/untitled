import mode
import datetime


star_time = datetime.datetime.now()

path = '/Users/yh/Desktop/分析测试文件/gztx_gz_07.xls'
table_name = 'gztx_gz_07'

value, type = mode.read_excel(path)
create_table_sql = mode.create_table_sql(table_name, value, type)
print('生成表语句：  ' + create_table_sql)
print('---' * 20)
mode.execute_sql(create_table_sql)
print('生成表%s' % table_name)
print('---' * 20)

mode.insert_exc_sql(table_name, value)

end_time = datetime.datetime.now()
time = end_time - star_time
print('消耗时间' + str(time))


