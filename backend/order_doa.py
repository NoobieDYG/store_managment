from datetime import date
from mysql_connector import sql_con_obj

def insert_order(connection,order):
    cursor=connection.cursor()
    order_query=('INSERT INTO `orders` (`customer_name`, `total`, `date_time`) VALUES (%s,%s,%s)')
    order_data=(order['customer_name'],order['total'],order['date_time'])
    cursor.execute(order_query,order_data)
    order_id=cursor.lastrowid

    order_details_query=('INSERT INTO order_details (order_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)')
    order_details_data=[]

    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
            
        ])
    
    cursor.executemany(order_details_query, order_details_data)


    connection.commit()
    cursor.close()
    return order_id

def get_all_orders(connection):
    cursor=connection.cursor()
    query=('Select * from orders')
    cursor.execute(query)
    response=[]
    for (order_id,customer_name,total,date_time) in cursor:
        response.append({
            'order_id':order_id,
            'customer_name':customer_name,
            'total':total,
            'date_time':date_time
        })
    cursor.close()
    return response
def get_order_details(connection):
    cursor=connection.cursor()

    query='SELECT order_details.order_id,products.product_name,order_details.quantity,products.price_per_unit,order_details.total_price FROM order_details LEFT JOIN products ON order_details.product_id = products.product_id;' #where order_details.order_id=%s
    #data=(order_id,)
    cursor.execute(query)
    data=cursor.fetchall()
    records=[]
    for(order_id, product_name, quantity, price_per_unit, total_price) in data:
        records.append({
            'order_id': order_id,
            'product_name': product_name,
            'quantity': quantity,
            'price_per_unit': price_per_unit,
            'total_price': total_price
        })
    #print(records)
    cursor.close()
    return (records)


if __name__=='__main__':

    from mysql_connector import sql_con_obj

    connection=sql_con_obj()
    '''print(insert_order(connection,{
        'customer_name': 'raju',
        'total': 800,
        'date_time': date.today(),
        'order_details':[{
            'product_id': 2,
            'quantity': 2,
            'total_price': 50
        }]
    }))'''
    #print(get_all_orders(connection))