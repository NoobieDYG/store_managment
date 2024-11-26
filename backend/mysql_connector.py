import mysql.connector
__con_obj=None
def sql_con_obj():
    __con_obj=mysql.connector.connect(user='root', password='1234',host='127.0.0.1',database='store')
    if __con_obj==None:
        return __con_obj