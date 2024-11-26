import datetime
import mysql.connector

__cnx = None

def sql_con_obj():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='1234',host = '127.0.0.1', database='store')

  return __cnx