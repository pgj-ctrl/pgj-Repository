#select,update,delete,retrieve
import pymysql

#创建到服务器的连接
conn = pymysql.connect(
    host= 'localhost',user='root',
    password='tedu.cn',db= 'nsd2006',
    charset= 'utf8mb4'
)

# 创建游标。游标像文件对象一样，通过文件对象对文件读写；通过游标对数据库进行增删改查
cursor = conn.cursor()


# 编写sql语句
# 查询
# select1 = "SELECT id, dep_name FROM departments"
# cursor.execute(select1)
# result1 = cursor.fetchone()    # 取出一行数据
# result2 = cursor.fetchmany(2)  # 继续取出2行数据
# result3 = cursor.fetchall()    # 继续取出剩余全部数据
# print(result1)
# print('*' * 30)
# print(result2)
# print('*' * 30)
# print(result3)
#####################################################
#修改
# update1 = "UPDATE departments SET dep_name= %s WHERE dep_name= %s"
# cursor.execute(update1,('人力资源部', '人事部'))
###########################################
# delete1 = "DELETE FROM departments WHERE id = %s"
# cursor.execute(delete1,(5,))

# 如果执行的是增删改查操作需要确认
conn.commit()

# 关闭
cursor.close()
conn.close()