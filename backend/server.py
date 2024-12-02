from flask import Flask,request,jsonify,render_template
from flask_cors import CORS
import python_doa
import mysql_connector
import order_doa
import um_doa
import json
app=Flask(__name__,static_folder="C:\\Users\\Affaan Jaweed\\Desktop\\sotre\\frontend\\static",template_folder="C:\\Users\\Affaan Jaweed\\Desktop\\sotre\\frontend")
CORS(app)

con_obj=mysql_connector.sql_con_obj()
@app.route('/index')
def hello():
    return render_template('index.html')

@app.route('/orders')
def showorders():
    return render_template('orders.html')

@app.route('/products')
def showprodcuts():
    return render_template('products.html')

@app.route('/')
def index():
    return 'welcome to store managment system, type /index to view home page'


@app.route('/getProduct', methods=['GET'])
def get_product():
    
    products=python_doa.get_all(con_obj)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getUom',methods=['GET'])
def get_um():
    um=um_doa.get_um(con_obj)
    response=jsonify(um)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/deleteProduct', methods=['POST'])

def delete_product():
    return_id = python_doa.delete_product(con_obj, request.form['product_id'])
    response=jsonify({
        'product_id': return_id
    })

    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/insertProduct',methods=["POST"])

def insert_product():
    insertion=python_doa.add_product(con_obj,json.loads(request.form['data']))
    response=jsonify({
        'product_id': insertion
    })

    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/insertorder',methods=['POST'])
def insert_order():
    order_data=request.get_json()
    insertion=order_doa.insert_order(con_obj,(order_data['data']))
    response=jsonify({
        'order_id':insertion
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/getallorder',methods=['GET'])
def get_all_orders():
    orders=order_doa.get_all_orders(con_obj)
    response=jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getorderdetail',methods=['GET'])
def get_order_details():
    order_detail=order_doa.get_order_details(con_obj)
    response=jsonify(order_detail)
    return response

if __name__=='__main__':
    print("Starting python flask server for store managment")
    app.run(port=5000,debug=True)