from mysql_connector import sql_con_obj
import mysql_connector
def get_all(connection):
    
    cursor=connection.cursor()
    query='SELECT products.product_id,products.product_name,products.um_id,products.price_per_unit,um.um_name from products inner join um on products.um_id=um.um_id'
    cursor.execute(query)
    response=[]
    for (product_id,product_name,um_id,price_per_unit,um_name) in cursor:
        response.append(
            {
                'product_id':product_id,
                'name':product_name,
                "um_id":um_id,
                "um_name":um_name,
                'price':price_per_unit

            }
        )
    return response
    con_obj.close()
def add_product(connection,product):
    cursor=connection.cursor()
    query='INSERT INTO products (product_name, um_id, price_per_unit) VALUES (%s,%s,%s);'
    data=(product['product_name'],product['um_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid


if __name__=='__main__':
    connection=sql_con_obj()
    print(get_all(connection))
    print(add_product(connection,{
        'product_name':'spinach',
        'um_id':'1',
        'price_per_unit':'67'
    }))