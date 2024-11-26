import mysql.connector

def get_all():
    con_obj=mysql.connector.connect(user='root', password='1234',host='127.0.0.1',database='store')
    cursor=con_obj.cursor()
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

if __name__=='__main__':
    print(get_all())