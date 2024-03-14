import mysql.connector
import time


if __name__ == "__main__": 
  mydb1 = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="5170Ill$",
    database="mydatabase"
  )

  cursor = mydb1.cursor()

  cursor.execute('''
      CREATE TABLE IF NOT EXISTS users(
      
          name TEXT NOT NULL,    
          password INT NOT NULL,
          status TEXT NOT NULL

      );
      ''')
  cursor.execute('''
      CREATE TABLE IF NOT EXISTS quiz(
      
          name TEXT NOT NULL,
          root TEXT NOT NULL,
          code TEXT NOT NULL    

      );
      ''')
  cursor.execute('''
      CREATE TABLE IF NOT EXISTS questions(
      
          name TEXT NOT NULL,
          quiz TEXT NOT NULL,    
          questions TEXT NOT NULL
      );
      ''')
  
  print("finish")
    