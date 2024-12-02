def get_um(connection):
    cursor=connection.cursor()

    query=('Select * from um')
    cursor.execute(query)
    response=[]
    for(um_id,um_name) in cursor:
        response.append({
            'um_id':um_id,
            'um_name':um_name
        })
    cursor.close()
    return response
if __name__=='__main__':

    from mysql_connector import sql_con_obj

    connection=sql_con_obj()
    x=get_um(connection)
    print(list(x))