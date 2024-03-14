import mysql.connector


if __name__ == "__main__":

  mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="5170Ill$"
  )

  cursor1 = mydb.cursor()
  cursor1.execute("CREATE DATABASE IF NOT EXISTS mydatabase;")

  mydb.close()
  print("finish")
