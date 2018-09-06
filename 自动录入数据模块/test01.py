import pymysql  # 导入 pymysql
import pandas as pd
import datetime


star_time = datetime.datetime.now()
#连接数据库
db = pymysql.connect(host="127.0.0.1", user="jdf", password="12345", db="pymysql_db", port=3306)

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
sql = '''
select c.*,
d.tc_zk,
c.sum_zc*d.tc_zk,
d.dx /c.ysb_days dx
from
(select a.*,
b.ysb_days,
b.ssb_days,
b.dx_days,
b.sg_date,
b.lz_date
 from 
(SELECT 
a.cercent,
a.area,
a.date,
sum(a.cj_fee * a.cj_zk) sum_cb,
a.emp_no,
a.emp_name,
sum(a.cz_num) sum_zc
FROM pymysql_db.gzl_gz_07 a
group by 
a.cercent,
a.area,
a.date,
a.emp_no,
a.emp_name) a ,
pymysql_db.user_gz_07 b
where a.emp_name = b.emp_name
) c ,
pymysql_db.gztx_gz_07 d
where c.sum_zc*c.ysb_days between d.cz_min and d.cz_max;
'''

data = pd.read_sql(sql,db)
data.to_csv('/Users/yh/Desktop/分析测试文件/广州呼出成本收入计算.csv',encoding="gb2312")

# data.to_csv('/Users/yh/Desktop/分析测试文件/广州6月人员产值明细.csv')
end_time = datetime.datetime.now()
print(end_time-star_time)