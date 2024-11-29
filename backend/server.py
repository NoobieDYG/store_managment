from flask import Flask,request,jsonify
import python_doa
import mysql_connector

app=Flask(__name__)

con_obj=mysql_connector.sql_con_obj()
@app.route('/hello')
def hello():
    return "hello, how is you the"


@app.route('/')
def index():
    return 'welcome to store managment system'


@app.route('/getProduct', methods=['GET'])
def get_product():
    
    products=python_doa.get_all(con_obj)
    response=jsonify(products)
    #response.headers.add('Access-Control-Allow-Origin','*')
    return response







if __name__=='__main__':
    print("Starting python flask server for store managment")
    app.run(port=5000)